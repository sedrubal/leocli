#!/usr/bin/env python
# -*- encoding: utf-8  -*-
# PYTHON_ARGCOMPLETE_OK

"""
leo - a console translation script for https://dict.leo.org
"""

from __future__ import print_function

"""
Copyright (c) 2012 Christian Schick

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__authors__ = "Christian Schick, Sedrubal"
__copyright__ = "Copyright 2013, Christian Schick"
__license__ = "MIT"
__version__ = "1.4.1"
__maintainer__ = "Christian Schick"
__email__ = "github@simperium.de"

from bs4 import BeautifulSoup
import requests
import argparse
import sys
import six
try:
    import autocomplete
except ImportError:
    pass

API = "https://dict.leo.org/dictQuery/m-vocab/{lang}de/query.xml"
DEFAULTPARAMS = {
    'tolerMode': 'nof',
    'lp': 'enable',
    'rmWords': 'off',
    'rmSearch': 'on',
    'searchLoc': '0',
    'resultOrder': 'basic',
    'multiwirdShowSingle': 'on',
    'lang': 'de',
}


def parse_args():
    """
    Parse arguments
    :return: the parsed arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('words',
                        action='store',
                        nargs='+',
                        metavar='word',
                        type=str,
                        help="the words you want to translate")
    parser.add_argument('-l', '--lang',
                        action='store',
                        dest='language',
                        metavar='lang',
                        type=str,
                        default='en',
                        choices=['en', 'fr', 'es', 'it',
                                 'ch', 'ru', 'pt', 'pl'],
                        help="the language to translate to or from")

    if 'autocomplete' in locals():
        autocomplete(parser)

    args = parser.parse_args()

    return args


def get(search, language='en'):
    """Queries the API and returns a lists of result string pairs"""
    params = {
        'search': '+'.join(search),
    }
    params.update(DEFAULTPARAMS)
    req = requests.get(API.format(lang=language), params=params)
    if req.status_code is not 200:
        print("[!] The API seems to be down", file=sys.stderr)
        exit(1)

    content = BeautifulSoup(req.text, "xml")
    results = []
    for section in content.sectionlist.findAll('section'):
        if int(section['sctCount']) > 0:
            for entry in section.findAll('entry'):
                res0 = entry.find('side', attrs={'hc': '0'})
                res1 = entry.find('side', attrs={'hc': '1'})
                if res0 and res1:
                    results.append((res0.repr.getText(),
                                    res1.repr.getText()))
            results.append(('---', '---'))
    del results[-1]  # remove last separator
    return results


def print_result(results):
    """Prints the result to stdout"""
    widest = (max(len(x[0]) for x in results), max(len(x[1]) for x in results))
    for (lang0, lang1) in results:
        if lang0 == lang1 == '---':
            # separator
            print('-' * (widest[0] + widest[1] + 4))
        else:
            space = " " * (widest[0] - len(lang0))
            print(six.text_type("{lang0}{space} -- {lang1}").format(
                lang0=lang0, space=space, lang1=lang1))


def main_entry():
    """the main function"""
    args = parse_args()
    res = get(args.words, args.language)
    if len(res):
        print_result(res)
    else:
        print("[!] No matches found for '%s'" % "', '".join(args.words),
              file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    sys.exit(main_entry())
