#Name: Huan-Yun Chen
#Course: CSCI 4140
#Date: 4/7/2018
#Description: project task 2

import  argparse, json, os
from collections import defaultdict
import json

#========================================================================================================================
def main() : 
	parser = argparse.ArgumentParser(description='Simple hand-crafted dialog state tracker baseline.')
	parser.add_argument('--dataset', dest='dataset', action='store', metavar='DATASET', required=True, help='The dataset to analyze')
	parser.add_argument('--dataroot',dest='dataroot',action='store',required=True,metavar='PATH', help='Will look for corpus in <destroot>/<dataset>/...')
	args = parser.parse_args()

	source = os.getcwd()
	fileListName = os.path.join(os.path.join(os.getcwd(),"scripts/config"),args.dataset+".flist")
	fileList = open(fileListName)  # opens flist file
	outputFile = open("part2.py","w")	#output file
	for fName in fileList :        # iterate through each dialog
		fName = fName[0:len(fName)-1]
		call = json.load(open(os.path.join(os.path.join(source,args.dataroot),os.path.join(fName,"log.json"))))
		label = json.load(open(os.path.join(os.path.join(source,args.dataroot),os.path.join(fName,"label.json"))))
		# iterate through each dialog turn; 
		# call is the data from the actual interaction (log.json)
		# label is the data provided by after dialog labeling (label.json)
		prevCurrent=[]
		firstTime=1
		print("File Name:"+fName)
		for turn,turnLabel in zip(call["turns"],label["turns"]) :
			eachTurn={}
			a=[]
			d=[]
			m=[]
			current=[]
			
			#prevent adding if act is cant help
			for i in turn['output']["dialog-acts"]:
				act=i['act']
				if act == 'canthelp':
					continue

			#first time in each turn just add all conditions
			if firstTime == 1:
				for each in turnLabel['goal-labels']:
					key = each
					value = turnLabel['goal-labels'][each]
					tup = (key,value)
					current.append(tup)
					a.append(tup)
					firstTime = 0
				eachTurn['m']=m
				eachTurn['d']=d
				eachTurn['a']=a
			else:
				for each in turnLabel['goal-labels']:
					key = each
					value = turnLabel['goal-labels'][each]
					tup=(key,value)
					exist =0
					#loop through the previous and determine to add,modified,or delete
					for k,v in prevCurrent:
						if k == key:
							exist=1
							if not value == v:
								m.append(tup)
								current.append(tup)
								prevCurrent.remove((k,v))
							elif value == v:
								current.append(tup)
								prevCurrent.remove((k,v))
						elif not k == key:
							exist=0
					if exist == 0:
						a.append(tup)
						current.append(tup)
				if not len(prevCurrent) == 0:
					for k,v in prevCurrent:
						d.append((k,v))
				eachTurn['m']=m
				eachTurn['d']=d
				eachTurn['a']=a
			print(eachTurn)
			outputFile.write(json.dumps(eachTurn))
			outputFile.write("\n")
			prevCurrent=current
		outputFile.write("**************************************************************\n")
		print ("**************************************************************")

if __name__ == '__main__':
	main()
