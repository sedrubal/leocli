from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import sys
from cgi import escape
from HTMLParser import HTMLParser

def get(search):
    mask = "http://dict.leo.org/ende?lang=de&search=%s"
    url = urlopen(mask % search.replace(" ", "+"))
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Missing keywords"
        sys.exit(255)
    get("+".join(
        escape(x).encode('ascii', 'xmlcharrefreplace') for x in sys.argv[1:]))
