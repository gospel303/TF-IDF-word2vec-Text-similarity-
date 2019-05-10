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

def read_sentence(filename):
    """读取一个文件并转换为一行,并去符号"""
    sentenceline = []
    with io.open(filename, 'r', encoding='utf-8') as f:
        sentenceline =  f.read().replace('\n', '').replace('\t', '').replace('\u3000', '').replace('<','').replace('>','').replace('(','')\
                    .replace(')','').replace('?','').replace('，','').replace('　　　　　','')\
                    .replace('：','').replace('　','').replace('“','').replace('”','').replace('.','').replace('、','').replace('》','').replace('《','')\
                    .replace('（','').replace('）','').replace(']','').replace('[','').replace('］','').replace('［','')
        return sentenceline

# txt转为list
def eachLine(fileName):
    with io.open(fileName, "r", encoding='utf-8') as f:
        lines = f.readlines()
        return (lines)#获得lines


def M_cosine(v1,v2):

    v1=np.array(v1)
    v2=np.array(v2)

    sim=1-spatial.distance.cosine(v1,v2)
    return sim

# 计算相似度并返回前五
def count_similar(sentencetxt,dictlines,TopK = 5):
#句子处理  暂定sentence是txt文件，打开之后做读为一行，去符号之后，就进入tf和w2v获得向量一个
    sentenceline = read_sentence(sentencetxt)
    # 按行处理 取一个文本的前100关键词
    tups = jieba.analyse.extract_tags(sentenceline, topK=100, withWeight=True, allowPOS=())
    numtups = len(tups)  # 实际取的关键词数
    i = 0
    word_xweight = 0
    model = gensim.models.Word2Vec.load('/home/fangqin/yf/tfidf/tmp/w2vmodel')
    while i < numtups:  # 遍历每一个关键词 i是关键词数
        word = tups[i][0]
        weight = tups[i][1]
        try:
            tryw2v = model[word]
        except KeyError:
            tryw2v = 0
        word_xweight = word_xweight + (weight * tryw2v)
        i = i + 1
        try:
            sentence_w2v = word_xweight / numtups
        except ZeroDivisionError:
            print ("该文件没有内容")


    dict_sims = {}#存储{sim:i}
    sim_list = []#存储sim从大到小

    for i in range(len(dictlines)):
        # dict_sim {相似度：文本序号}
        dict_sims[M_cosine(sentence_w2v,dictlines[i])] = i
    # 相似度排序[] 获得从大到小
    sim_list = sorted(dict_sims.keys(),reverse=True)

    for i in range(TopK):
        # 获得名称
        dictnames = pickle.load(open('/home/fangqin/yf/tfw2v/tmp/dictallname','rb'))
        names = dictnames[dict_sims[sim_list[i]]]
        print ("相似文本名称："+names+"  "+"相似度："+bytes(sim_list[i]))

if __name__ == '__main__':

    # 要测试的一个文件txt
    sentencetxt= '/home/fangqin/yf/tfw2v/chulitxt/(2012)滨中法委赔字第2号-1.txt'
    dictlines = pickle.load(open('/home/fangqin/yf/tfw2v/tmp/dictlines','rb'))
    count_similar(sentencetxt,dictlines)












