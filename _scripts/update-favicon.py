#!/usr/bin/env python2.7
# Copyright (c) 2015 Sebastian Wiesner <swiesner@lunaryorn.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import print_function

import os
from subprocess import check_call
from argparse import ArgumentParser


SOURCE_DIRECTORY = os.path.join(os.path.dirname(__file__), os.pardir)
ICON_HEAD_FILE = os.path.join(SOURCE_DIRECTORY, '_includes', 'head-icon.html')
SIZES = [16, 32, 64, 96, 196]
BASENAME = 'icon-{size}'


def generate_favicons(source_file):
    inkscape = ['inkscape',
                '--without-gui',
                '--export-area-page',
                '--export-background=white']
    generated_icons = []
    for size in SIZES:
        filename = BASENAME.format(size=size) + '.png'
        target = os.path.join(SOURCE_DIRECTORY, filename)
        args = ['--export-png=' + target,
                '--export-width={0}'.format(size),
                source_file]
        check_call(inkscape + args)
        generated_icons.append((size, filename))
    return generated_icons


def make_link(size, filename):
    return '<link rel="icon" sizes="{size}x{size}" href="/{filename}">'.format(
        size=size, filename=filename)


def write_head_icon_include(icons):
    links = [make_link(size, filename) for size, filename in icons]
    with open(ICON_HEAD_FILE, 'w') as sink:
        sink.write('\n'.join(links))


def main():
    parser = ArgumentParser()
    parser.add_argument('source_file')
    args = parser.parse_args()

    icons = generate_favicons(args.source_file)
    write_head_icon_include(icons)


if __name__ == '__main__':
    main()
