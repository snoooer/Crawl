#!/usr/bin/env python
#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import os

class mzitu:
    headers = {"User-Agent":
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"}

    def getAllUrl(self,url):
        html = requests.get(url,headers =self.headers)
        bsObj = BeautifulSoup(html.text,"lxml")
        all_url = bsObj.find("div",{"class":"all"}).findAll("a")
        for a in all_url:
            title = a.get_text()
            print(u'开始保存:',title)
            path = str(title).replace("?","_")
            self.mkdir(path)
            href = a.attrs["href"]
            self.getPageUrl(href)

    def getPageUrl(self,href):
        html = requests.get(href,headers = self.headers)
        bsObj = BeautifulSoup(html.text,"lxml")
        pages = bsObj.find("div",{"class":"pagenavi"}).findAll("span")[-2].get_text()
        for page in range(1,int(pages) + 1):
            img_url = href + "/" + str(page)
            self.getImg(img_url)

    def getImg(self,img_url):
        html = requests.get(img_url,headers = self.headers)
        bsObj = BeautifulSoup(html.text,"lxml")
        src = bsObj.find("div",{"class":"main-image"}).find("img").attrs["src"]
        self.save(src)

    def save(self,src):
        name = src[-9:]
        img = requests.get(src,headers = self.headers)
        fin = open(name,"ab")
        fin.write(img.content)
        fin.close()

    def mkdir(self,path):
        path = path.strip()
        os.makedirs(os.path.join("/home/john/Downloads/mzitu",path))
        os.chdir("/home/john/Downloads/mzitu/" + path)

mzi = mzitu()
url ="http://www.mzitu.com/all"
mzi.getAllUrl(url)



