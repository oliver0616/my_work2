# Name: Huan-Yun Chen
# soundex.py template
# CSCI 4140

import sys
import nltk
import re

# Define any global helper strings at this point

# Define tuple list and mapping code to create dictionary for consonant
# transformations at this point

# function that takes token, transforms it into its new form, and returns it
# YOU WRTIE THE FUNCTION

def wordmap(token) :
	token = token.lower()
	#Step 1: Save first letter, remove 'h' and 'w'
	firstLetter = token[:1]
	sOneToken=""
	for character in token[1:]:
		if (not character == "h") and (not character == "w"):
			sOneToken += character	
	sOneToken = firstLetter+ sOneToken
	#Step 2: Replace consonants with digits
	sTwoToken=""
	numOne =['b','f','p','v']
	numTwo =['c','g','j','k','q','s','x','z']
	numThree =['d','t']
	numFour =['l']
	numFive =['m','n']
	numSix =['r']	
	for t in sOneToken:
		if t in numOne:
			sTwoToken+='1'		
		elif t in numTwo:
			sTwoToken+='2'
		elif t in numThree:
			sTwoToken+='3'
		elif t in numFour:
			sTwoToken+='4'
		elif t in numFive:
			sTwoToken+='5'
		elif t in numSix:
			sTwoToken+='6'
		else:
			sTwoToken+=t
	#Step 3: Replace adjacent same digits with one digit
	sThreeToken=""
	previous=""
	for character in sTwoToken:
		if not previous == character:
			sThreeToken += character
		previous = character
	#Step 4: Remove occurrences[a,e,i,o,u,y] except first letter
	sFourToken=sThreeToken[:1]
	removeSet=['a','e','i','o','u','y']
	for character in sThreeToken[1:]:
		if not character in removeSet:
			sFourToken += character
	#Step 5: Replace first symobal if it's digit
	sFiveToken=""
	numList=['1','2','3','4','5','6']
	if sFourToken[:1] in numList:
		sFiveToken=firstLetter.upper()
	else:
		sFiveToken=sFourToken[:1].upper()
	sFiveToken+=sFourToken[1:]
	#Step 6: Append 3 zero if result contain less than 3 digits
	sSixToken=sFiveToken
	if len(sFiveToken)<4:
		for i in range(3):
			sSixToken+='0'
	result = sSixToken[:4]

	return result

# Driver code for the program
# sys.argv[1] should be the name of the input file
# sys.argv[0] will be the name of this file

for line in open(sys.argv[1]).readlines():
	text = nltk.word_tokenize(line.lower())
	for token in text:
		#print(token)
		print (wordmap(token),end=' ')
	print()  # This prints new line at the end of processing a line

