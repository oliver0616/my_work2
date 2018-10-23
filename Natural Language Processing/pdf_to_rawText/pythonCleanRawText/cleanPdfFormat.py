import itertools
import codecs

def main():
    inputString =''
    inputFile =open('test.txt','r')
    outputFile =open('output.txt','w')
    for line in inputFile:
        if not line == '\n' or not line ==' ':
            line = line.replace('\n','')
            line = line.replace('{','')
            line = line.replace('}','')
            line = line.replace('&','')
            line = line.replace('\\','')
            line = line.replace('\"','')
            inputString = inputString+line

    newString = '\"pdf\":\"'+inputString+'\"}'
    outputFile.write(newString)
    outputFile.close()
    
def cleanFormat():
    inputString =''
    inputFile =open('test.json','r')
    outputFile=codecs.open("result.json","w","utf-8")

    for line in inputFile:
        inputString += line
    outputFile.write(inputString)
    outputFile.close()

main()
cleanFormat()
