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

require 'rake/dsl_definition'
require 'rake/file_list'
require 'pathname'

ICON_SIZES = [16, 32, 64, 96, 196]
ICONS = Rake::FileList[ICON_SIZES.map { |size| "icon-#{size}.png" }]
LOGO_HEIGHT = 30

namespace :icons do
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
    Pathname.new(t.name).write(
      t.prerequisites.map { |icon| make_link(icon) }.join("\n"))
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
