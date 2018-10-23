from supwsd.wsd import SupWSD

def allWords():
	text = 'The human brain is quite proficient at word-sense disambiguation.'
	for sense in SupWSD().senses(text):
		#print('Word: {}\tLemma: {}\tPOS: {}\tSense: {}'.format(sense.word, sense.lemma, sense.pos, sense.key()))
		print(sense.miss)

def specific():
	text = 'The human ' + SupWSD.SENSE_TAG + 'brain' + SupWSD.SENSE_TAG + ' is quite proficient at word-sense disambiguation. The fact that natural language is formed '+ SupWSD.SENSE_TAG+'in a way'+ SupWSD.SENSE_TAG+' that requires so much of it is a ' + SupWSD.SENSE_TAG + 'reflection' + SupWSD.SENSE_TAG + ' of that neurologic reality.'
	for sense in SupWSD().senses(text):
		print('Word: {}\tLemma: {}\tPOS: {}\tSense: {}'.format(sense.word, sense.lemma, sense.pos, sense.key()))

def retrieveAll():
	text = 'The human brain is quite proficient at word-sense disambiguation.'

	for sense in SupWSD().senses(text,True):
		print('Word: {}\tLemma: {}\tPOS: {}\tSense: {}'.format(sense.word, sense.lemma, sense.pos, sense.key()))
		for result in sense.results:
			print('Sense {}\tProbability: {}'.format(result.key, result.prob))

print("start")
choice = '1'
#choice = input("Number:")
if choice == '1':
	allWords()
elif choice == '2':
	specific()
elif choice == '3':
	retrieveAll()
