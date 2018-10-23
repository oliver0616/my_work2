#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 2/6/2018
#Tabs: 8

import nltk
from nltk import word_tokenize

silly ='newly formed bland ideas are inexpressible in an infuriating way'
bland = silly.split(' ')			#split silly
second =""					#store second words
space=' '					#represent space


for w in bland:					#store second character of each string into second
	second = second+w[1]

space.join(bland)			#use join to join words back together

tokens = word_tokenize(silly)		#print string in alphabatical order
print(sorted(tokens))
