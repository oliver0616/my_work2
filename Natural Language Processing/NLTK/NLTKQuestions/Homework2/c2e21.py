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
entries = nltk.corpus.cmudict.entries()

def the_syllables(inputText):
	result =[]
	counter = len(inputText)
	text = inputText
#read the entire word and try to match them with the entries, reduce the word character by character
#append the answer to the result list
	while not (counter == 0):
		for each in entries:
			if text == each[0]:
				result.append(each)
				counter = len(inputText)-counter
				text = inputText[counter:]
		counter =counter-1
		text = text[:-1]
		if counter < 0:
			break
		print text
	print result
		
the_syllables("statement")
the_syllables("break")
the_syllables("ridiculous")
the_syllables("read")
