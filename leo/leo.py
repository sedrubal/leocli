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
__version__    = "1.4"
__maintainer__ = "Christian Schick"
__email__      = "github@simperium.de"

################################################################################

from BeautifulSoup import BeautifulSoup, Tag
from urllib2 import urlopen
import sys
from cgi import escape
from HTMLParser import HTMLParser
from PySide.QtWebKit import QWebPage
from PySide.QtGui import QApplication
from PySide.QtCore import QUrl

class WebPage(QWebPage):
    def __init__(self, url):
        self.__app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.__app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.__app.quit()

def getlang(td):
    """Returns the language attribute of a td tag."""
    lang = None
    for attr, value in td.attrs:
        if attr == "lang":
            lang = value
            break
    return lang

def istag(obj):
    """Tests if an object is an instance of BeautifulSoup.Tag."""
    return isinstance(obj, Tag)

def nospans(tag):
    """Checks that the given tag contains no <span> subtags."""
    spans = False
    for subtag in tag.contents:
        if istag(subtag):
            spans = subtag.name == "span"
        if spans:
            break
    return not spans

def get(search):
    mask = "http://dict.leo.org/dictQuery/m-vocab/ende/de.html?searchLoc=0&lp"\
           "=ende&lang=de&directN=0&search=%s&resultOrder=basic&"\
           "multiwordShowSingle=on"
    url = mask % search.replace(" ", "+")
    p = WebPage(url)
    html = p.frame.toHtml().encode('ascii', 'ignore')
    content = BeautifulSoup(html)
    p = HTMLParser()
    result_en = content.findAll(
            "td", attrs={"data-dz-attr": "relink", "lang": "en"})
    result_de = content.findAll(
            "td", attrs={"data-dz-attr": "relink", "lang": "de"})
    outlines = []
    left = None
    right = None
    widest = 0
    for i in range(0, len(result_en)):
        if nospans(result_en[i]):
            c = result_en[i].contents
            left = "".join(p.unescape(x.text if istag(x) else x) for x in c)
            c = result_de[i].contents
            right = "".join(p.unescape(x.text if istag(x) else x ) for x in c)
            left = left.strip()
            right = right.strip()
            if len(left) > widest:
                widest = len(left)
            outlines.append((left, right))
    if len(outlines) > 0:
        widest = max(len(x[0]) for x in outlines)
        print "\n".join(
                x + (" " * (widest - len(x))) + " -- " + y for x, y in outlines)
    else:
        print "No matches found for '%s'" % search

################################################################################

def main_entry():
    if len(sys.argv) < 2:
        print "Missing keywords"
        sys.exit(255)
    get("+".join(
        escape(x).encode('ascii', 'xmlcharrefreplace') for x in sys.argv[1:]))

################################################################################

if __name__ == "__main__":
    sys.exit(main_entry())
