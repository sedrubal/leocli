#!/usr/bin/python
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


"""
================================================================================
               leo - a german<->english language translation script
================================================================================

This setup script installs leo system-wide.
"""

from setuptools import setup, find_packages
import os
from leo import leo

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name="leo",
        packages=find_packages(),
        entry_points = {
            "console_scripts" : ["leo = leo.leo:main_entry"]
            },
        author=leo.__author__,
        author_email=leo.__email__,
        license=leo.__license__,
        description="leo - a german<->english language translation script",
        long_description=read("README"),
        url="http://github.com/Hydrael/leo",
        version=leo.__version__,
        install_requires=["BeautifulSoup"])
