# 一个简答的存取csv文件的例子
# 使用 字典 来读取和写入数据

import csv

def reader(filepath) :
    with open(filepath) as th :
        read=csv.DictReader(th)
        for item in read :
            print(item)

def writer() :
    fields=['ItemID', 'Name', 'Description', 'Owner', 'Borrower', 'Datelent', 'DateReturned']
    words=['7', 'Scarifier', 'Qualitys, stainless steel', 'Anne', 'Mike', '12/25/2013', '']

    with open('tooldesc2.csv','w',newline='') as td :
        dic={}
        for i in range(len(fields)) :
            dic[fields[i]]=words[i]
        write=csv.DictWriter(td,fieldnames=fields,dialect='excel')

        write.writerow(dic)



if __name__=='__main__' :
    #reader('./toolhire.csv')
    writer()