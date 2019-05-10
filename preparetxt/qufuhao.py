# -*- coding:utf-8 -*-

import sys
import jieba
import io
reload(sys)
sys.setdefaultencoding("utf-8")
'''
完全版
去掉了所有的符号包括各种空格（粘贴过来就行了）
'''

# 也完成了分词  注释掉了

def text_to_wordlist(text):
    words = list(jieba.cut(text.strip(), cut_all=False))
    return (" ".join(words))

def eachLine(fileName,fileName2):
        with io.open(fileName, "r", encoding='utf-8') as f:
            lines = f.readlines()

        with io.open(fileName2, "w", encoding='utf-8') as f_w:
            for line in lines:
                strline = line.strip()\
                    .replace('。','').strip(':').strip('.').strip(';').replace(' ','').replace('\t', '').replace('\u3000', '').replace('<','').replace('>','').replace('(','')\
                    .replace(')','').replace('?','').replace('，','').replace('　　　　　','')\
                    .replace('：','').replace('　','').replace('“','').replace('”','').replace('.','').replace('、','').replace('》','').replace('《','')\
                    .replace('（','').replace('）','').replace(']','').replace('[','').replace('］','').replace('［','').replace('；','')
                print (strline)

                # print (text_to_wordlist(strline))

                # f_w.write(text_to_wordlist(strline)+'\n')
                f_w.write(strline + '\n')


if __name__ == '__main__':
    # 需要去空格的文件
    fileName="/home/fangqin/yf/tfw2v/chulitxt/413all一行.txt"
    # 输出文件
    fileName2="/home/fangqin/yf/tfw2v/chulitxt/413all去空格.txt"
    eachLine(fileName,fileName2)


