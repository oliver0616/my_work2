import os

def transfer(fileName):
    inputFile = open(fileName,"r")
    allString = ""
    #outputFile = open("","w")
    
    for line in inputFile:
        allString = allString + line
        
    splitString = allString.split(".I")

    counter = 0
    currentDir=os.getcwd()
    currentDir=currentDir + "\\output"
    miss = []
    for each in splitString:
        if not each == " ":
            completeName = os.path.join(currentDir,str(counter)+".txt")
            outputFile = open(completeName,"w")
            outputFile.write(each)
            outputFile.close()
            print("File "+completeName + " has completed")
        else:
            miss.append(counter)
        counter +=1
    print(miss)
#============================================================================
def query(fileName):
    inputFile = open(fileName,"r")
    allString = ""
    #outputFile = open("","w")
    
    for line in inputFile:
        allString = allString + line
        
    splitString = allString.split(".I")
    counter = 0
    currentDir=os.getcwd()
    currentDir=currentDir + "\\output"
    miss = []
    for each in splitString:
        splitAgain = each.split(".W")
        #print(len(splitAgain))
        if not len(splitAgain) == 1:
            #print(splitAgain[1])
            inp = splitAgain[1];
            listOfChar=["+","-","&","|","!","(",")","{","}","[","]","^",'"',"~","*","?",":","\\"]
            for ch in listOfChar:
                inp = inp.replace(ch,"");
            completeName = os.path.join(currentDir,str(counter)+".txt")
            outputFile = open(completeName,"w")
            outputFile.write(inp)
            outputFile.close()
            print("File "+completeName + " has completed")
        else:
            miss.append(counter)
        counter +=1
    print(miss)

#============================================================================
def main():
    #query("cran.qry")
    transfer("cran.all.1400")
main()
