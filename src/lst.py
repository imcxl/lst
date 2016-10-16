# -*- coding: utf-8 -*-
'''
Created on 2016年10月16日

Usage:

1. python ls.py
2. python ls.py path

列出当前目录 / 指定目录中的文件列表，使用 pylsy 来显示。

@author: cxl
'''
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
from pylsy import pylsytable

import os
import time
import stat


def timeFormat(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))


def modeFormat(m):
    if stat.S_ISREG(m):           #判断是否一般文件
        return 'Regular file.'
    elif stat.S_ISLNK (m):         #判断是否链接文件
        return 'Shortcut.'
    elif stat.S_ISSOCK (m):        #判断是否套接字文件    
        return 'Socket.'
    elif stat.S_ISFIFO (m):        #判断是否命名管道
        return 'Named pipe.'
    elif stat.S_ISBLK (m):         #判断是否块设备
        return 'Block special device.'
    elif stat.S_ISCHR (m):         #判断是否字符设置
        return 'Character special device.'
    elif stat.S_ISDIR (m):         #判断是否目录
        return 'directory.'


def sizeFormat(s):
    unit = ['b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'] # KMGTPEZY
    unit_len = len(unit)
    index = 0
    while s > 1024 and index < unit_len - 1:
        s = s / 1024
        index += 1
    return str(round(s, 2)) + ' ' + unit[index]


def lsPath(path=os.path.abspath('.')):
    attributes = ["Mode", "Name", "Size", "Create", "Modify"] 
    table = pylsytable(attributes)
    table.add_data("Mode", [])
    table.add_data("Name", [])
    table.add_data("Size", [])
    table.add_data("Create", [])
    table.add_data("Modify", [])

    files = os.listdir(path)      
    for f in files:
        table.append_data("Name", [f])
        stat = os.stat(os.path.join(path, f))
        table.append_data("Mode",[modeFormat(stat.st_mode)])
        table.append_data("Size",[sizeFormat(stat.st_size)])
        table.append_data("Create",[timeFormat(stat.st_ctime)])
        table.append_data("Modify",[timeFormat(stat.st_mtime)])

    return table


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print lsPath(sys.argv[1])
    else:
        print lsPath()
