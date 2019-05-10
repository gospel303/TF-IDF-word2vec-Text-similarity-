# TF-IDF-word2vec-Text-similarity-
TF-IDF+Word2vec做文本相似度计算，最好是长文本
使用说明：
给出目标文本的txt文件，与众多被对比文本计算相似度，获得相似度最高的前五个文档并给出相似度

先创建两个文件夹 tmp 和 tmp2 来分别存储中间文件和word2vec训练的model

预处理：
用preparetxt中的文件处理原始文件--我的原始文件为：每个被对比文档是一个txt文件，utf-8编码
preparetxt文件夹中，有将所有txt文件一个转换为一行存在一个大txt文件的文件totext.py；去空格和符号的文件qufuhao.py；分词的文件fenci.py。
根据你的原始文件进行按需处理。
最后获得：
存放了所有去空格、去符号、分词的被对比文档的大txt文件--用来训练w2v模型
存放了所有去空格、去符号的被对比文档的大txt文件--用来获得每个文档的最终向量

获得这些文件后先后运行
trainw2v.py --用来训练w2v模型
trainembedding.py --用来获得被对比文档的词向量
tfidf.py --用来计算相似度

输入文件均在最下方，输入后即可
