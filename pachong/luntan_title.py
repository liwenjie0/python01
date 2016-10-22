# 操作系统windows10，python 3.5
# 获取kukupig论坛帖子的标题和链接

#未完成！！！！！！！！！！！！！！！！！！！！
import urllib.request
from bs4 import BeautifulSoup
import threading
import re

class MyThread(threading.Thread) :
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
    def run(self):
        threading.Thread.apply(self.func,self.args)
        print()

def  running(url) :
    # lock.acquire()
    html=urllib.request.urlopen(url)
    if html.status_code==200 :
        print()
    html_text=html.read()
    soup=BeautifulSoup(html_text,"html.parser")
    with open('./item.txt','a+',encoding='gbk') as f :
        for link in soup.find_all('tbody',id=re.compile('normalthread_.+')) :
            print(link.find('a','s xst').get_text())
            print(link.find('a','s xst').get('href'))
            str0=link.find('a','s xst').get_text().encode('gbk',errors='ignore').decode('gbk')
            f.write(str0)
            f.write('\t'+link.find('a','s xst').get('href'))
            f.write('\n')
        f.close()

n=0
raw_url='http://bbs.kukupig.com/forum.php?mod=forumdisplay&fid=6&page='
url_list=[]
for i in range(1,10) :
    url_list.append(raw_url+str(i))
    print(url_list[i-1])
    print(i)
    #running(url_list[i-1])



if __name__=='__main__' :
    thread_list=[MyThread(running,(url,)) for url in url_list]
    for t in thread_list :
        t.setDaemon(True)
        t.start()
    for i in thread_list :
        i.join()
        print("process ended")
