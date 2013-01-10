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
"""


################################################################################
# AUTHORSHIP INFORMATION
################################################################################
__author__     = "Christian Schick"
__copyright__  = "Copyright 2013, Christian Schick"
__license__    = "MIT"
__version__    = "1.1"
__maintainer__ = "Christian Schick"
__email__      = "github@simperium.de"

################################################################################

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import sys
from cgi import escape
from HTMLParser import HTMLParser

def get(keywords):
    """Gets the translations and meanings for a string containing keywords.
    @param keywords Single string containing keywords to search for.
    """
    mask = "http://dict.leo.org/ende?lang=de&search=%s"
    url = urlopen(mask % keywords.replace(" ", "+"))
    content = BeautifulSoup(url)
    p = HTMLParser()
    # all <td> tags with valign="middle" are potential results
    result = content.findAll("td", attrs={"valign": "middle"})
    # actual results all start with &nbsp; so we filter for those
    outlines = []
    left = None
    right = None
    widest = 0
    # buffer hits in list for later string formatting
    for i, c in enumerate(filter(lambda x: x.contents[0] == u'&nbsp;', result)):
        texts = filter(lambda x: hasattr(x, "text"), c.contents[1:])
        if i % 2 == 0:
            left = " ".join(p.unescape(x.text) for x in texts)
        else:
            right = " ".join(p.unescape(x.text) for x in texts)
            if len(right) > widest:
                widest = len(right)
            outlines.append((right, left))

    print "\n".join(
            x + (" " * (widest - len(x))) + " -- " + y for x, y in outlines)

################################################################################

def main_entry():
    if len(sys.argv) < 2:
        print "Missing keywords"
        return 255
    get("+".join(
        escape(x).encode('ascii', 'xmlcharrefreplace') for x in sys.argv[1:]))
    return 0

################################################################################

if __name__ == "__main__":
    sys.exit(main_entry())
