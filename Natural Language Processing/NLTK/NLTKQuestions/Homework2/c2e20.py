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
def word_freq(word,name):
	f = nltk.probability.FreqDist(nltk.corpus.brown.words(categories = name))
	result = freq[word]
	return result
