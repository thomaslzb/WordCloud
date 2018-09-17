#-*-coding:utf-8-*-

import jieba
import jieba.analyse
# jieba.enable_parallel(4)
# 开启并行分词模式，参数为并行进程数:4 ,but unable to run on Windows

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, ImageColorGenerator


# The function for processing text with Jieba
# 前50个高频词汇
def jieba_processing_txt(text):
    result = jieba.analyse.textrank(text, topK=50, withWeight=True)
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]
    return keywords

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__)+'/files' if "__file__" in locals() else os.getcwd()

# Chinese fonts must be set 这个字库必须要
font_path = d + '/fonts/SourceHanSerifK-Light.otf'
original_img = d + '/luxun_color.jpg'
original_txt = d + '/luxun_book.txt'

#files is exist?
if not (os.path.isfile(font_path) and os.path.isfile(original_img) \
                and  os.path.isfile(original_txt)) :
    if not os.path.isfile(stopwords_path):
        print ("stopwords_path or pngFile does not found!")
    if not os.path.isfile(font_path):
        print ("font_path or pngFile does not found!")
    if not os.path.isfile(imgname1):
        print ("original img or pngFile does not found!")
    os._exit(0)

# the path to save worldcloud
imgname1 = d + '/LuXun.jpg'
imgname2 = d + '/LuXun_colored.jpg'

# read the mask / color image taken from

back_coloring = imread(path.join(d, original_img))
txt_book = path.join(original_txt)

#  Read the whole text. ‘rb’文件以二进制的方式读入
text = open(txt_book, 'rb').read()

wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
               max_font_size=100, random_state=42, width=1000, height=860, margin=2,)


# wc.generate(jieba_processing_txt(text))

wc.generate_from_frequencies(jieba_processing_txt(text))

# create coloring from image
image_colors_default = ImageColorGenerator(back_coloring)

# save wordcloud
wc.to_file(path.join(d, imgname1))

# recolor wordcloud and show
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")


plt.figure()
plt.imshow(back_coloring, interpolation="bilinear")
plt.axis("off")

# show
# we could also give color_func=image_colors directly in the constructor
# create coloring from image
image_colors_byImg = ImageColorGenerator(back_coloring)
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
plt.axis("off")

# save wordcloud
wc.recolor(color_func=image_colors_byImg).to_file(path.join(d, imgname2))

plt.show()

