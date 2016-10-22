# 简单的食用config文件的例子

import configparser as cp

def write() :
    conf=cp.ConfigParser()
    conf['DEFAULT']={'lending_period':0 ,'max_value':0}
    conf['Fred']={'max_value':200}
    conf['Anne']={'lending_period':30}
    with open('tool.ini','w') as tool :
        conf.write(tool)

def read() :
    conf=cp.ConfigParser()
    print(conf.read('tool.ini'))
    print(conf.sections())
    print(conf['DEFAULT']['max_value'])
    print(conf['Anne']['lending_period'])
    print(conf['Fred']['max_value'])



if __name__=='__main__' :
    read()
    print('OK ')