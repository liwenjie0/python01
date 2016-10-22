# 一个简单的读取csv文件的例子

import csv

def reader(filepath) :
    with open(filepath) as th :
        toolreader=csv.reader(th)
        list0=list(toolreader)
        for list1 in list0 :
            print(list1)

items=[
    ['1','Lawnmower','Small Hover mower','Fred','$150','Excellent','2012-01-05'],
    ['2','Lawnmower','Rider-on mower','Mike','$371','Fair','2012-04-01'],
    ['2','Bike','BMX bike','Joe','$200','Good','2013-03-22'],
    ['4','Drill','Heavy duty hammer','Ron','$100','Good','2013/10/28']
]
def writer(filepath) :
    with open(filepath,'w',newline='') as tooldata :
        tooldwrite=csv.writer(tooldata)
        for item in items :
            tooldwrite.writerow(item)

if __name__=='__main__' :
    writer('./tooldesc.csv')