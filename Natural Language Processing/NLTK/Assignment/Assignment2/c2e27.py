#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 2/10/2018
#Tabs: 8
#The following program is program in Python 3
#output:
'''
Average polysemy for noun = 1.28
Average polysemy for verb = 2.19
Average polysemy for adverb = 1.25
Average polysemy for adjective = 1.41
'''
#==========================================================
#Imports
from __future__ import division
from nltk.corpus import wordnet as wn
#==========================================================

def calculateAverage(typeName):
	allSynsets = wn.all_synsets(typeName)
	totalWords =[]
	for s in allSynsets:		#loop thro synsets and store the words into totalWords
		totalWords= totalWords+s.lemma_names()
	wordsCount = len(set(totalWords))

	totalSensesCount = 0
	t = set(totalWords)
	for s in t:		#loop thro the synset of the word and store the them counts of them
		eachSensesCount=len(wn.synsets(s,typeName))
		totalSensesCount = totalSensesCount + eachSensesCount

	average = totalSensesCount / wordsCount
	return average

averageNum = calculateAverage('n')		#passing in Noun
print("Average polysemy for noun = "+format(averageNum,'.2f'))
averageNum = calculateAverage('v')		#passing in Verb
print("Average polysemy for verb = "+format(averageNum,'.2f'))
averageNum = calculateAverage('r')		#passing in Adverb
print("Average polysemy for adverb = "+format(averageNum,'.2f'))
averageNum = calculateAverage('a')		#passing in Adjective
print("Average polysemy for adjective = "+format(averageNum,'.2f'))
