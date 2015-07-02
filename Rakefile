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

namespace :images do
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

  task :all, [:inkscape] => ['_includes/head-icon.html', 'images/logo.png']
end

namespace :manual do
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
    after_body_open = customizations['AFTER_BODY_OPEN']
    customizations['AFTER_BODY_OPEN'] =
      IO.read('_includes/ga.html') + after_body_open
    customizations
  end

  desc 'Update the HTML manual from "srcdir" for "version" (default latest)'
  task :update, [:srcdir, :version, :texi2any] do |_, args|
    args.with_defaults(version: 'latest', texi2any: 'texi2any')
    ensure_srcdir args
    source = Pathname.new(args.srcdir).join('doc').join('flycheck.texi')
    target = "manual/#{args.version}/"
    rm_r(target)
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
end

namespace :docs do
  desc 'Update credits.md from srcdir'
  task 'credits.md', [:srcdir] do |_, args|
    ensure_srcdir args
    source = Pathname.new(args.srcdir).join('CREDITS.md')
    target = '_includes/credits.md'
    Rake.rake_output_message "cp #{source} #{target}"
    File.open(target, 'w') do |sink|
      File.foreach(source).drop(3).each { |line| sink.write(line) }
    end
  end

  desc 'Update changes.md from srcdir'
  task 'changes.md', [:srcdir] do |_, args|
    ensure_srcdir args
    source = Pathname.new(args.srcdir).join('CHANGES.md')
    cp(source, '_includes/changes.md')
  end

  desc 'Update all documents from srcdir'
  task :all, [:srcdir] => %w(changes.md credits.md)
end

namespace :dev do
  desc 'Install all dependencies to _vendor/'
  task :deps do
    sh 'bundler', 'install', '--path', '_vendor', '--binstubs=_vendor/bin'
  end

  CLOBBER << '.bundle'
  CLOBBER << '_vendor'
  CLOBBER << '_site'

  desc 'Preview the site at http://localhost:4000'
  task :preview do
    sh '_vendor/bin/jekyll', 'serve', '-w'
  end
end
