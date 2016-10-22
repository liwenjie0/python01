#
# 爬取糗事百科热门模块内容

import re,urllib.request
from bs4 import BeautifulSoup

class Getqiubai(object) :

    def __init__(self):
        object.__init__(self)
        self.url='http://www.qiushibaike.com/8hr/page/3/?s=4923541'
        self.html=urllib.request.urlopen(self.url)
        self.content=self.html.read(100)
        print(self.content)



if __name__=='__main__' :
    obj0=Getqiubai()