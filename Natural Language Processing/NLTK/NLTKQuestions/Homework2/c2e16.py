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
def lexDivTable(corpus):
	result=[]	
	for each in corpus.categories():
		result.append(len(corpus.words(categories=each))/len(set(corpus.words(categories=each))))

	cf =nltk.ConditionalFreqDist(
	(name,count)
	for name in corpus.categories()
	for count in result
	)
	return cf.plot()
lexDivTable(nltk.corpus.brown)
