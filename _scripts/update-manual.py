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

import sys
import os
import errno
import shutil
from subprocess import CalledProcessError, check_call
from itertools import chain


SOURCE_DIRECTORY = os.path.join(os.path.dirname(__file__), os.pardir)
BUILD_DIRECTORY = os.path.join(SOURCE_DIRECTORY, '_tmp')
MANUAL_DIRECTORY = os.path.join(SOURCE_DIRECTORY, 'manual')


CUSTOMIZATION = {
    # Wrap our container around the body
    'AFTER_BODY_OPEN': '<div class="container">',
    'PRE_BODY_CLOSE': '</div>',
    # Add classes to Texinfo rulers
    'BIG_RULE': '<hr class="texinfo-big-rule"/>',
    'DEFAULT_RULE': '<hr class="texinfo-default-rule"/>',
    # Point up from top to the right place
    'TOP_NODE_UP_URL': '/index.html',
    # Suggest that we use HTML 5.  We don't do actually, but we want the browse
    # to think that we do
    'DOCTYPE': '<!DOCTYPE html>',
}


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise


def include_path(filename):
    return os.path.join(SOURCE_DIRECTORY, '_includes', filename)


def read_extra_customization():
    extra_customization = {}
    extra_head = []
    with open(include_path('head-css.html'), 'r') as source:
        extra_customization['CSS_LINES'] = source.read()
    for filename in ['head-static.html', 'head-icon.html']:
        with open(include_path(filename), 'r') as source:
            extra_head.append(source.read())
    extra_customization['EXTRA_HEAD'] = '\n'.join(extra_head)
    with open(include_path('ga.html'), 'r') as source:
        after_body = source.read() + CUSTOMIZATION['AFTER_BODY_OPEN']
        extra_customization['AFTER_BODY_OPEN'] = after_body
    return extra_customization


def build_manual(source_file, extra_customization=None):
    customization = dict(CUSTOMIZATION)
    customization.update(extra_customization or {})
    variables = [['--set-customization-variable', var + '=' + value]
                 for var, value in customization.iteritems()]
    texi2any = ['texi2any', '--html', '-o', BUILD_DIRECTORY]
    check_call(texi2any + list(chain(*variables)) + [source_file])


def copy_images(source_file):
    image_directory = os.path.join(os.path.dirname(source_file), 'images')
    shutil.copytree(image_directory, os.path.join(BUILD_DIRECTORY, 'images'))


def sync_manual(version='latest'):
    target_directory = os.path.join(MANUAL_DIRECTORY, version)

    ensure_directory(target_directory)
    check_call(['rsync', '-r', '--delete',
                # Append slash to copy the contents of the directory with rsync
                BUILD_DIRECTORY + '/',
                target_directory])


class Colors(object):           # pylint: disable=R0903
    red = '\033[31m'
    green = '\033[32m'
    reset = '\033[0m'
    bold = '\033[1m'


def success(s):
    return Colors.green + Colors.bold + s + Colors.reset


def fail(s):
    return Colors.red + Colors.bold + s + Colors.reset


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('source_file')
    parser.add_argument('-v', '--version', default='latest')
    args = parser.parse_args()

    # Clean the build directory
    if os.path.exists(BUILD_DIRECTORY):
        shutil.rmtree(BUILD_DIRECTORY)
    ensure_directory(BUILD_DIRECTORY)

    try:
        print('Building {0.source_file} for version {0.version}... '.format(args),
              end='')
        extra_customization = read_extra_customization()
        build_manual(args.source_file, extra_customization=extra_customization)
        copy_images(args.source_file)
        sync_manual(version=args.version)
        print(success('success'))
    except CalledProcessError:
        print(fail('FAILED'))
        sys.exit(1)
    finally:
        shutil.rmtree(BUILD_DIRECTORY)


if __name__ == '__main__':
    main()
