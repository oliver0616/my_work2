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
def atLeastThree(corpus):
	listOfWords = FreqDist([word.lower() for word in corpus])
	result=[]
	for w in listOfWords:
		if listOfWords[w] >= 3:
			result.append(w)
	print result
	return result
#example:		
atLeastThree(nltk.corpus.cess_esp.words())	
