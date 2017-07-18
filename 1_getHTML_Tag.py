#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError

def getTittle(url):
    try:
        html = urlopen(url)
    except(HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        tltle = bsObj.body.h1
    except AttributeError as e:
        return None
    return tltle

def getSiteHTML(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    return BeautifulSoup(html.read(),"lxml")

html = getSiteHTML('http://www.jianshu.com/p/47f3824b1285')
print(html)

title = getTittle('http://www.jianshu.com/p/47f3824b1285')
if title == None:
    print('Title could not found')
else:
    print(title)