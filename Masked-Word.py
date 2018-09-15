#-*-coding:utf-8-*-
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support
# running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
org_txt = d + "/files/alice.txt"
org_img = d + "/files/alice_mask.png"

#check file exists
if os.path.isfile(org_txt) and os.path.isfile(org_img):
    # Read the whole text.
    text = open(path.join(d, org_txt)).read()
else:
    print ("TxtFile or pngFile does not found!")
    os._exit(0)

# read the mask image
# taken from
alice_mask = np.array(Image.open(path.join(d,org_img)))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "alice.png"))

"""
# show in one figure
plt.figure()
plt.subplot(1,2,1)
plt.imshow(alice_mask, cmap=plt.cm.prism, interpolation='bilinear')
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")

"""

#show original png
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.prism, interpolation='bilinear')
plt.axis("off")

# show marked png
plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")

plt.show()
