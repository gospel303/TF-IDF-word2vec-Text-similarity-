# -*- coding: utf-8 -*-

import io
import os
import sys
import pickle
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

'''
完全版
把一个文件夹里的所有txt文件每个写成一行，放在一个TXT文件里。
这里额外加了存储名字序号的词典的部分
'''

def _read_file(filename):
    """读取一个文件并转换为一行"""
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.read().replace('\n', '').replace('\t', '').replace('\u3000', '')

def save_file(dirname,sava_file,picklefile):
    f_train = io.open(sava_file, 'w', encoding='utf-8')
    cat_dir = os.path.join(dirname)
    files = os.listdir(cat_dir)
    count = 0
    dictname_list = {}

    for cur_file in files:
        # print (cur_file)
        dictname_list[count] = cur_file
        filename = os.path.join(cat_dir, cur_file)
        content = _read_file(filename)
        count = count +1

        f_train.write(content + '\n')
    with open(picklefile, "w") as pkf:
        pickle.dump(dictname_list,pkf)
    f_train.close()

if __name__ == '__main__':
    # 输入的文件夹
    dirname ='/home/fangqin/yf/413alltxt'
    #存储的txt文件,这里定好名字就行，不存在会自行创造，存在应该会重写
    save_file_name='/home/fangqin/yf/tfw2v/chulitxt/413all一行.txt'
    # 存储txt文件的名字和序号对应的词典  {序号：名字}
    picklefile = '/home/fangqin/yf/tfw2v/tmp/dictallname'
    save_file(dirname,save_file_name,picklefile)
    #输出有多少行
    print(len(io.open(save_file_name, 'r', encoding='utf-8').readlines()))

