#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 1/28/2018
#Tabs: 8

#==========================================================
import nltk
from nltk.corpus import brown
#from nltk.book import *
# prefix needed for graphics on department server
import matplotlib
matplotlib.use('TKagg')
from nltk import FreqDist, ConditionalFreqDist
#==========================================================

cfd = nltk.ConditionalFreqDist(
(keyword, fileid[:4])
#words looking for
for keyword in ['men', 'women', 'people']
#loop thro txt
for fileid in nltk.corpus.state_union.fileids()
#loop thro words
for word in nltk.corpus.state_union.words(fileid)
#change lower case and are they start with keyword
if word.lower().startswith(keyword))

cfd.plot()
