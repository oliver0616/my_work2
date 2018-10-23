#Name: Huan-Yun Chen
#Course: CSCI 4140
#Date: 4/18/2018
#Description: project task 3, the question is: Does the top slu hypothosis repeat info from previous utterence?
#compare each previous and current highest score slu hypothesis and determine if there is any change, provide changes

import  argparse, json, os
from collections import defaultdict

#========================================================================================================================
def main() : 
	parser = argparse.ArgumentParser(description='Simple hand-crafted dialog state tracker baseline.')
	parser.add_argument('--dataset', dest='dataset', action='store', metavar='DATASET', required=True, help='The dataset to analyze')
	parser.add_argument('--dataroot',dest='dataroot',action='store',required=True,metavar='PATH', help='Will look for corpus in <destroot>/<dataset>/...')
	args = parser.parse_args()

	source = os.getcwd()
	fileListName = os.path.join(os.path.join(os.getcwd(),"scripts/config"),args.dataset+".flist")
	fileList = open(fileListName)  # opens flist file
	outputFile = open("part3.py","w") #outputfile
	for fName in fileList :        # iterate through each dialog
		fName = fName[0:len(fName)-1]
		call = json.load(open(os.path.join(os.path.join(source,args.dataroot),os.path.join(fName,"log.json"))))
		label = json.load(open(os.path.join(os.path.join(source,args.dataroot),os.path.join(fName,"label.json"))))
		# iterate through each dialog turn; 
		# call is the data from the actual interaction (log.json)
		# label is the data provided by after dialog labeling (label.json)
		print("File Name:"+fName)
		outputFile.write("File Name:"+fName+"\n")
		firstTime=1
		prevCurrent=[]
		
		for turn,turnLabel in zip(call["turns"],label["turns"]) :
			print("Turn-Index:"+str(turn['turn-index']))
			outputFile.write("Turn-Index:"+str(turn['turn-index'])+"\n")
			current=[]
			final=''
			#first time in each turn just add all conditions
			if firstTime == 1:
				if len(turn['input']['live']['slu-hyps'][0]['slu-hyp']) == 0:
					final = "Empty"
					tup=('empty','empty')
					current.append((tup))
				else:
					each = turn['input']['live']['slu-hyps'][0]['slu-hyp']
					for slot in each:
						#print(slot)
						if not slot["slots"]:
							final = "Empty"
							tup=('empty','empty')
							current.append((tup))
						else:
							slots=slot['slots']
							for i in slots:
								category = i[0]
								value = i[1]
								tup=(category,value)
								current.append(tup)
								firstTime = 0
							final='Slu-Hyp(Start):'
							for c,v in current:
								final = final+"("+c+","+v+"), "

			else:
				if len(turn['input']['live']['slu-hyps'][0]['slu-hyp']) == 0:
					final = "Empty"
					tup=('empty','empty')
					current.append((tup))
				else:
					each = turn['input']['live']['slu-hyps'][0]['slu-hyp']
					for slot in each:
						if not slot["slots"]:
							final = "Empty"
							tup=('empty','empty')
							current.append((tup))
						else:
							slots=slot['slots']
							for i in slots:
								category = i[0]
								value = i[1]
								tup=(category,value)
								current.append(tup)
								for prevEach in prevCurrent:
									prevCategory,prevValue=prevEach
									if prevCategory == category and prevValue==value:
										final='No'
									else:
										final='Yes'
			prevCurrent=current
			if final == 'Yes':
				final = final+": "
				for c,v in current:
					final = final+"("+c+","+v+"), "
				print(final)
				outputFile.write(final+"\n")
			elif final == 'No':
				print(final)
				outputFile.write(final+"\n")
			else:
				print(final)
				outputFile.write(final+"\n")
		outputFile.write("**************************************************************\n")
		print ("**************************************************************")

if __name__ == '__main__':
	main()
