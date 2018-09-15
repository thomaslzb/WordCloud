#+++++++++++++++++++++++++++++++++++++++++++++++
#Author: thomaslzb (thomaslzbuk@gmail.com
#
#(C) 2018
#Version 1.0
#+++++++++++++++++++++++++++++++++++++++++++++++
import jieba.analyse # 这是一个中文分词工具库

#encoding=gbk
lyric_txt= ''
f=open('./励志歌曲歌词.txt','r')
for i in f:
    lyric_txt += f.read()

result=jieba.analyse.textrank(lyric_txt,topK=50,withWeight=True)
keywords = dict()
for i in result:
  keywords[i[0]]=i[1]
print(keywords)