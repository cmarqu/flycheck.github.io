# Copyright (c) 2015  Sebastian Wiesner <swiesner@lunaryorn.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

require 'pathname'
require 'rake/clean'

def ensure_srcdir(args)
  fail 'srcdir argument missing' if args.srcdir.nil?
end

# File rules
ICON_SIZES = [16, 32, 64, 96, 196]
ICONS = Rake::FileList[ICON_SIZES.map { |size| "icon-#{size}.png" }]
LOGO_HEIGHT = 30

def make_link(icon)
  /^icon-(?<size>\d+)\.png$/ =~ icon
  "<link rel=\"icon\" sizes=\"#{size}x#{size}\" href=\"/#{icon}\">"
end

rule(/icon-.*\.png/, [:inkscape] => ['flycheck.svg']) do |t, args|
  args.with_defaults(inkscape: 'inkscape')
  /^icon-(?<size>\d+)\.png$/ =~ t.name
  sh(args.inkscape, '--without-gui', '--export-area-age',
     '--export-background=white', "--export-png=#{t.name}",
     "--export-width=#{size}",
     t.source)
end

file '_includes/head-icon.html' => ICONS do |t|
  IO.write(t.name, t.prerequisites.map { |icon| make_link(icon) }.join("\n"))
end

file 'images/logo.png', [:inkscape, :logo_height] =>
                        ['flycheck.svg'] do |t, args|
  args.with_defaults(inkscape: 'inkscape', logo_height: LOGO_HEIGHT)
  sh('--without-gui', '--export-area-drawing',
     '--export-background-opacity=0,0',
     "--export-height=#{args.logo_height}",
     "--export-png=#{t.name}",
     t.source)
end

namespace :init do
  CLOBBER << '.bundle'
  CLOBBER << 'vendor'

  desc 'Install dependencies via bundle'
  task :dependencies do
    sh 'bundle', 'install', '--path', 'vendor'
  end

  desc 'Install git submodules'
  task :submodules do
    sh 'git', 'submodule', 'update', '--init'
  end
end

desc 'Initialize the repository'
task init: ['init:dependencies', 'init:submodules']

namespace :build do
  CLOBBER << '_site'

  desc 'Build the site'
  task :site do
    sh 'bundle', 'exec', 'jekyll', 'build'
  end

  desc 'Build all images'
  task :images, [:inkscape] => ['_includes/head-icon.html', 'images/logo.png']

  # Build the manual
  DEFAULT_CUSTOMIZATIONS = {
    # Wrap our container around the body
    'AFTER_BODY_OPEN' => '<div class="container">',
    'PRE_BODY_CLOSE' => '</div>',
    # Add classes to Texinfo rulers
    'BIG_RULE' => '<hr class="texinfo-big-rule"/>',
    'DEFAULT_RULE' => '<hr class="texinfo-default-rule"/>',
    # Point up from top to the right place
    'TOP_NODE_UP_URL' => '/index.html',
    # Suggest that we use HTML 5.  We don't do actually, but we want the browse
    # to think that we do
    'DOCTYPE' => '<!DOCTYPE html>'
  }

  def customizations
    customizations = DEFAULT_CUSTOMIZATIONS.clone
    customizations['CSS_LINES'] = IO.read('_includes/head-css.html')
    customizations['EXTRA_HEAD'] = ['head-static.html', 'head-icon.html']
                                   .map { |file| IO.read("_includes/#{file}") }
                                   .join("\n")
    tracking = IO.read('_includes/ga.html')
    customizations['AFTER_BODY_OPEN'] =
      customizations['AFTER_BODY_OPEN'] + tracking
    customizations
  end

  desc 'Update the HTML manual from "srcdir" for "version" (default latest)'
  task :manual, [:srcdir, :version, :texi2any] do |_, args|
    args.with_defaults(version: 'latest', texi2any: 'texi2any')
    ensure_srcdir args
    source = Pathname.new(args.srcdir).join('doc').join('flycheck.texi')
    target = "manual/#{args.version}/"
    rm_rf(target)
    mkdir_p(target)
    customization_options =
      customizations
      .map { |var, value| ['--set-customization-variable', "#{var}=#{value}"] }
      .flatten
    sh(*[args.texi2any, '--html', '-o', target] +
        customization_options +
        [source.to_path])
    cp_r(source.dirname.join('images').to_path, target)
  end

  # Build documents
  task 'authors.md', [:srcdir] do |_, args|
    ensure_srcdir args
    source = Pathname.new(args.srcdir).join('AUTHORS.md')
    target = '_includes/authors.md'
    Rake.rake_output_message "cp #{source} #{target}"
    File.open(target, 'w') do |sink|
      File.foreach(source).drop(3).each { |line| sink.write(line) }
    end
  end

  desc 'Update changes.md from srcdir'
  task 'changes.md', [:srcdir] do |_, args|
    ensure_srcdir args
    source = Pathname.new(args.srcdir).join('CHANGES.md')
    target = '_includes/changes.md'
    Rake.rake_output_message "cp #{source} #{target} (substituting issue references)"
    changelog = IO.read(source)
    changelog.gsub!(
      /(?<label>\[GH-(?<issue>\d+)\])/,
      '[\k<label>](https://github.com/flycheck/flycheck/issues/\k<issue>)')
    IO.write(target, changelog)
  end

  desc 'Update all documents from srcdir'
  task :documents, [:srcdir] => %w(changes.md authors.md)
end

desc 'Build everything'
task build: ['build:site']

namespace :verify do
  desc 'Run jekyll doctor'
  task :doctor do
    sh 'bundle', 'exec', 'jekyll', 'doctor'
  end

  desc 'Run GH Pages health-check'
  task :healthcheck do
    sh 'bundle', 'exec', 'github-pages', 'health-check'
  end

  desc 'Run SCSS Lint'
  task :lint do
    sh 'bundle', 'exec', 'scss-lint',
       '--config', '_sass/.scss-lint.yml', '_sass/'
  end

  desc 'Run HTML Proofer'
  task proof: ['build:site'] do
    sh 'bundle', 'exec', 'htmlproof', '_site/',
       '--disable-external',
       '--check-html',
       '--check-favicon'
  end
end

desc 'Verify the site'
task verify: ['verify:doctor',
              'verify:healthcheck',
              'verify:lint',
              'verify:proof']

namespace :run do
  desc 'Preview the site at http://localhost:4000'
  task :preview do
    sh 'bundle', 'exec', 'jekyll', 'serve', '-w', '-D', '--future'
  end
end
