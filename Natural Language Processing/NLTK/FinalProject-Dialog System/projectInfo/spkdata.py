#Name: Huan-Yun Chen
#Course: CSCI 4140
#Date: 4/7/2018
#Description: project task 1, created csv file name is "spkdata.csv"

import  argparse, json, os
from collections import defaultdict
import csv
import sluRes
from sluRes import sluResult

#=======================================================================================================================
#get the highest count and reutrn the result
def getHighestCount(inputList):
	firstTime = 1
	for each in inputList:
		if firstTime == 1:
			highestScore = each["score"]
			highestAsr = each["asr-hyp"]
			firstTime = 0
		else:
			asrHyp = each["asr-hyp"]
			score = each["score"]
			if score > highestScore:
				highestScore = score
				highestAsr = asrHyp
	result =(highestScore,highestAsr)
	return result

#=======================================================================================================================
#find the unique set of words
def uniqueSet(inputList):
	result =""
	for each in inputList:
		words = each["asr-hyp"]
		result = result +" "+ words
	return set(result.split())

#=======================================================================================================================
def main() :
	parser = argparse.ArgumentParser(description='Simple hand-crafted dialog state tracker baseline.')
	parser.add_argument('--dataset', dest='dataset', action='store', metavar='DATASET', required=True, help='The dataset to analyze')
	parser.add_argument('--dataroot',dest='dataroot',action='store',required=True,metavar='PATH', help='Will look for corpus in <destroot>/<dataset>/...')
	args = parser.parse_args()

	source = os.getcwd()
	fileListName = os.path.join(os.path.join(os.getcwd(),"scripts/config"),args.dataset+".flist")
	fileList = open(fileListName)  # opens flist file
	csvFile = open("part1.csv","w",newline="")	#csv output file
	writer = csv.writer(csvFile)	#write of the csv file

	for fName in fileList :        # iterate through each dialog
		fName = fName[0:len(fName)-1]
		call = json.load(open(os.path.join(os.path.join(source,args.dataroot),os.path.join(fName,"log.json"))))
		label = json.load(open(os.path.join(os.path.join(source,args.dataroot),os.path.join(fName,"label.json"))))
		# iterate through each dialog turn; 
		# call is the data from the actual interaction (log.json)
		# label is the data provided by after dialog labeling (label.json)
		for turn,turnLabel in zip(call["turns"],label["turns"]) :
			print("Turn Number: "+str(turn["turn-index"]))
			print("Number of Words Spoken: "+ str(len(turn["output"]["transcript"].split())))
			asrScore,asr = getHighestCount(turn["input"]["live"]["asr-hyps"])
			print("Number of Words Highest Scored Live Speech Recognition Hypothesis: "+str(len(asr)))
			unique=uniqueSet(turn["input"]["live"]["asr-hyps"])			
			print("Total Number of Unique Words in Live Speech Recognition Hypothesis: "+str(len(unique)))
			uLabel=sluResult(turn,turnLabel)
			print("Understanding or Not:"+uLabel)
			data =[[turn["turn-index"],len(turn["output"]["transcript"].split()),len(asr),len(unique),uLabel]]
			writer.writerows(data)
		print ("**************************************************************")
	csvFile.close()
if __name__ == '__main__':
	main()
