#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 2/6/2018
#Tabs: 8

import nltk

inputList =['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
lengths =[]

for word in inputList:
	num = len(word)
	lengths.append(num)

print (inputList)
print(lengths)
