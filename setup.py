#!/usr/bin/env python

"""
leo - a console translation script for https://dict.leo.org/ .

This setup script installs leo.
"""

import os

from setuptools import find_packages, setup

from leo import leo

"""
Copyright (c) 2012 Christian Schick

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_requirements(filename="requirements.txt"):
    """Returns a list of all requirements."""
    text = read(filename)
    requirements = []
    for line in text.splitlines():
        req = line.split('#')[0].strip()
        if req != '':
            requirements.append(req)
    return requirements

setup(
    name="leo",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["leo = leo.leo:main_entry"]
    },
    author=leo.__authors__,
    author_email=leo.__email__,
    license=leo.__license__,
    description=leo.__doc__,
    long_description=read("README.md"),
    url="http://github.com/Hydrael/leo",
    version=leo.__version__,
    install_requires=get_requirements(),
)
