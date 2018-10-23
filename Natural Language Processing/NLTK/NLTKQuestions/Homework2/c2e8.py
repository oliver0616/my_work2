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
fd = nltk.ConditionalFreqDist([
(fileName, name[0])
#get the files
for fileName in ['female.txt', 'male.txt'] 
#loop thro namequit()
for name in nltk.corpus.names.words(fileName)
])
#display
fd.tabulate()
