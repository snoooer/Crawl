#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError,HTTPError
import re

def getHTML(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    bsObj = BeautifulSoup(html,"lxml")
    return bsObj

bsObj = getHTML('http://www.pythonscraping.com/pages/page3.html')
imgs = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for img in imgs:
    print(img)
    print(img["src"])