import itertools
import codecs

def mainFunction():
    bibFile = open('test.bib','r')
    bibString=""
    finalFile =codecs.open("result.json","w","utf-8")   #result File
    errorFile =open("errorFile.txt","w")                #error File
    indexCounter =0                                     #index counter
    duplicateCounter =0                                 #duplicate counter
    successCounter =0                                   #success counter

    for line in bibFile:
        if not (line =="\n" or line == "}\n" or line == "}"):
            line = line.strip()            
            line=line+'NEWLINE'
            bibString= bibString+line
    bibFile.close()
    data = typeResult(bibString,errorFile)
    for eachData in data: 
        result = convertData(eachData,errorFile)
        if result =="duplicate":
            duplicateCounter+=1
        else:
            indexCounter+=1
            index = "{\"index\":{\"_id\":\""+str(indexCounter)+"\"}}"
            #print(index)
            #print(result)
            finalFile.write(index+"\n")
            finalFile.write(result+"\n")
            successCounter+=1
    print("Data TransferSuccess:"+str(successCounter))
    print("Duplicate Data:"+str(duplicateCounter))
    errorFile.close()       
    finalFile.close()
    
#===============================================================================
#check class

def typeResult(input,errorFile):
    dataIn =0
    errorData =0
    finalResult=[]
    
    data=input.split("@")
    data.pop(0)
    for line in data:
        fewWords = line[0:15]
        exists =checkType(fewWords)
        if exists:
            dataIn +=1
            finalResult.append(line)
        else:
            errorData +=1
            errorLine = line.replace("NEWLINE","\n")
            errorLine = "This doesn't exists:\n"+errorLine+"\n"
            errorReturn(errorLine,errorFile)
            #print("This doesn't exists:\n"+errorLine+"\n")
    print("Read in Data:"+str(dataIn))
    print("Type not register:"+str(errorData))
            
    return finalResult

#---------------------------------------------------------------------
def checkType(input):
    exists = False
    types = ["online","inproceedings","article","techreport","book","phdthesis"]
    for check in types:
        exists = check.lower() in input.lower()
        if exists:
            return exists
    return exists
                
#================================================================================
def convertData(input,errorFile):
    attributeArray=[]
    result=""
    inside=True
    splitString = input.split("NEWLINE")
    for num,eachLine in enumerate(splitString, start=0):
        if num == 0 and not eachLine == "":
            firstLine=eachLine.replace(",","")
            firstLine=firstLine.replace("{","REPLACE")
            splitData=firstLine.split("REPLACE")
            firstLine="{\"datatype\":\""+splitData[0]+"\",\"key\":\""+splitData[1]+"\","
            result=result+firstLine
        else:
            if not eachLine=="}" and not eachLine=="":
                otherLine=eachLine.replace("{","")
                otherLine=otherLine.replace("}","")
                if not "=" in otherLine:
                    if inside:
                        result=result[:len(result)-1]
                        result=result[:len(result)-1]
                        inside = False
                    otherLine =otherLine.replace("&","")
                    otherLine =otherLine.replace("\\","")
                    otherLine =otherLine.replace("\"","")
                    result = result+" "+otherLine
                     
                else:
                    splitEqual = otherLine.split("=")   #split text to two parts attribute and their data
                    name = splitEqual[0]    #attribute
                    name = name.replace(" ","")
                    for each in attributeArray: #checking duplicate attributes
                        if name == each:
                            errorDa = input.replace("NEWLINE","\n")
                            errorDa = "Duplicate Attributes:\n"+errorDa+"\n"
                            errorReturn(errorDa,errorFile)
                            return "duplicate"
                    attributeArray.append(name)
                    name ="\""+name+"\":"

                    data=splitEqual[1]  #data
                    if data[-1:] == ",":
                        data = data[:len(data)-1] #take out comma at the end
                    data = data.replace("{","")
                    data = data.replace("}","")
                    if data[:1]==" " or data[:1]=="\t":
                        data = data[1:]           #take out space at front
                    data = data.replace("\"","")
                    data = data.replace("&","")
                    data = data.replace("\\","")
                    data ="\""+data+"\","

                    finalString =name+data
                    inside =True
                    result=result+finalString
    
    if inside == False:
        result = result[:len(result)-1]+"\"}"
    else:
        result = result[:len(result)-1]+"}"
   
    return result     

#================================================================================
def errorReturn(input,errorFile):
    errorFile.write(input)
               
#================================================================================
mainFunction()
