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
#store entries into es
es = nltk.corpus.cmudict.entries()
#store each word without pronunciation into eachWords
eachWords =[]
for w in es:
	eachWords.append(w[0])
#use set to find the unique word
distinct = set(eachWords)
print "Distinct Words: %d" %len(distinct)
#print "Distinct Words are:%i" %distinct
count = FreqDist(eachWords)
#store more than one pronunciation into moreThanOne
moreThanOne=[]
for more in eachWords:
	if(count[more] > 1):
		moreThanOne.append(more)
#calculation for fiction
a = len(moreThanOne)
b = len(distinct)
fraction = 19523/123455
print "Fraction: %f" %fraction
