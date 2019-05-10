# -*- coding:UTF-8 -*-
from gensim.models import word2vec
import numpy as np
from gensim import corpora
import gensim
import jieba
import io
import jieba.analyse
import pickle
from scipy import spatial
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# txt转为list
def eachLine(fileName):
    with io.open(fileName, "r", encoding='utf-8') as f:
        lines = f.readlines()
        return (lines)#获得lines


def get_sims(file_lines,picklefile):
    # 获得之前训练的w2v模型
    model = gensim.models.Word2Vec.load('/home/fangqin/yf/tfidf/tmp/w2vmodel')

    lines = eachLine(file_lines)
    dictlines = {}#存储每一行的最终向量
    j = 0#记录行数

    for line in lines:
        # 按行处理 取一个文本的前100关键词
        tups = jieba.analyse.extract_tags(line,topK=100,withWeight=True,allowPOS=())
        numtups = len(tups)#实际取的关键词数
        i = 0
        word_xweight = 0
        while i<numtups :#遍历每一个关键词 i是关键词数
            word = tups[i][0]
            weight = tups[i][1]
            try:
                tryw2v = model[word]
            except KeyError:
                tryw2v = 0
            word_xweight = word_xweight + (weight * tryw2v)
            i=i+1
        try:
            word_w2v_tf=word_xweight/numtups
        except ZeroDivisionError:
            print ("该文件没有内容")

        dictlines[j] = word_w2v_tf
        j = j+1
    with open(picklefile, 'w') as pks:
            pickle.dump(dictlines,pks)




if __name__ == '__main__':

    #被对比的文件，需要已经一行去空格的文件，不用分词
    file_lines = '/home/fangqin/yf/tfw2v/chulitxt/413all去空格.txt'
    # 存放被对比文件的词向量
    picklefile = '/home/fangqin/yf/tfw2v/tmp/dictlines'

    dictlines = get_sims(file_lines,picklefile)








