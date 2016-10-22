#coding:utf-8
#使用BeautifuolSoup获取豆瓣新片榜，口碑，票房 榜

import re,urllib.request
from bs4 import BeautifulSoup

class DBM(object) :
    def __init__(self,reg,html):
        self.reg,self.html=reg,html
    def __iter__(self):
        return self #instance self is iteration object,soreturn self

    def get(self):
        #print(self.reg)
        m_list=re.findall(self.reg,self.html)
        u_list=[]
        for abc in m_list :
            u_list.append(abc)
        return u_list

raw_url='https://movie.douban.com/chart'
html0=urllib.request.urlopen(raw_url)
content=html0.read()
f=open('./douban.txt','w',)
#设置正则表达式
reg_name=r'<img src=".*" alt="(.*)" class=""/>'
reg_introduction=r'<p class="pl">(.*?)</p>'
reg_score=r'<span class="rating_nums">(.*?)</span>'
reg_evalute=r'<span class="pl">\((.*)\)</span>'
print ('豆瓣新片排行榜')
print('-'*50)
f.write('豆瓣新片排行榜\n')
f.write('-'*50+'\n')

html=content.decode('utf-8',errors='ignore')
name = DBM(reg_name,html)
a=name.get()
introduction=DBM(reg_introduction,html)
b=introduction.get()
score=DBM(reg_score,html)
c=score.get()
evaluate = DBM(reg_evalute,html)
d=evaluate.get()

def index(num) :
    print(a[num],' ',b[num],' ','Score:%s'%(c[num]),' ',d[num])
    f.write(a[num]+' '+b[num]+' '+'Score:%s'%(c[num])+' '+d[num]+'\n')
    print()

nn =len(b)
#print(nn)
for x in range(nn) :
    print(x)
    index(x)


# use bs4
soup=BeautifulSoup(content,"html.parser")

#本周口碑榜
week=soup.find('div',id='ranking').find('ul',id='listCont2')
print('-'*80)
print("本周口碑榜...",soup.find('div',id='ranking').find('ul',id='listCont2')\
      .find('li').get_text())
f.write('-'*80+'\n'+\
        "本周口碑榜..."+soup.find('div',id='ranking').find('ul',id='listCont2').find('li').get_text()+\
        '\n')
for link in week.find_all('a') :
    print(link.get_text())
    f.write(link.get_text())

#北美票房榜影名
week_name=soup.find(name='div',id='ranking').find(name='ul',id='listCont1')
america=[]
for link in week_name.find_all('a') :
    america.append(link.get_text())
money=soup.find(name='div',id='ranking').find(name='ul',id='listCont1')
dollar=[]
for m in money.find_all('span') :
    dollar.append(m.get_text())
m_date=dollar.pop(0)

def split(num2) :
    print(america[num2],'-',dollar[num2])

print('-'*80)
print('北美票房榜。。。',m_date)
lens=len(america)
for i in range(lens) :
    split(i)

f.close()