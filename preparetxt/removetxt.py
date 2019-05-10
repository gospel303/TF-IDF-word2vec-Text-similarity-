# -*- coding:utf-8 -*-
import os
import shutil
'''
完全版
把文件名里有-1的文件都复制到另一个文件夹里
'''


oripath = "/home/fangqin/yf/413alltxt"
targetpath = "/home/fangqin/yf/413只有1"
files = os.listdir(oripath)
for f in enumerate(files):
    f=str(f[1])

    if f.find("-1")>=0 :

        shutil.copyfile(oripath+'/'+f, targetpath+'/'+f)

