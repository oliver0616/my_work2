import os

#please name your input cranfield file as "cran.all.1400". the program will create
# a "output.json" file in json format. the error data set would not be record into
#the output file and "errorReport.txt" will tell the user error information
# main
def main():
    #filepath=os.getcwd()+"\input"
    #input file name
    inputFile=open("cran.all.1400","r")
    newFile=""
    right=""

    outputFile=open("output.json","w")
    try:
        os.remove(os.getcwd()+"\errorReport.txt")
    except OSError:
        pass
    
    for each in inputFile:
        each=each.replace("\n"," ")
        newFile=newFile+each
    splitData=newFile.split(".I")
    
    for each in splitData:
        if not each =="":
            r=splitting(each,".T")
            num,left=r
            num=num.strip()
            if left =="ERROR":
                errorReport(each)
                continue
            r=splitting(left,".A")
            title,left=r
            title=title.strip()
            if left =="ERROR":
                errorReport(each)
                continue
            r=splitting(left,".B")
            author,left=r
            author=author.strip()
            if left =="ERROR":
                errorReport(each)
                continue
            r=splitting(left,".W")
            date,abstract=r
            date=date.strip()
            if abstract =="ERROR":
                errorReport(each)
                continue
            abstract=abstract.strip()

            title=jsonEscape(title)
            author=jsonEscape(author)
            date=jsonEscape(date)
            abstract=jsonEscape(abstract)
            
            index="{\"index\":{\"_id\":\""+str(num)+"\"}}"
            data="{\"title\":\""+title+"\","+"\"author\":\""+author+"\","+"\"date\":\""+date+"\","+"\"abstract\":\""+abstract+"\"}"
            outputFile.write(index+"\n")
            outputFile.write(data+"\n")
    outputFile.close()

#split function
def splitting(inputD,n):
    splitD=inputD.split(n)
    requireInfo=splitD[0]
    if len(splitD)==2:
        leftInfo=splitD[1]
    else:
        print("THERE IS ERROR TO THIS DATA WHILE SPLITTING "+n+":")
        print("The Split size: "+str(len(splitD)))
        leftInfo ="ERROR"
        print(inputD)
        print("======================================================")
    result=(requireInfo,leftInfo)
    return result

#json escape characters
def jsonEscape(inputData):
    inputData=inputData.replace("\""," ")     #replace "
    inputData=inputData.replace("\\"," ")     #replace \
    inputData=inputData.replace("\n"," ")     #replace newLine
    inputData=inputData.replace("\b"," ")     #replace backspace
    inputData=inputData.replace("\f"," ")     #replace form feed
    inputData=inputData.replace("\r"," ")     #replace carriage return
    return inputData

#error report
def errorReport(errorD):
    errorFile=open("errorReport.txt","a")
    errorFile.write("There is error in the following data:\n")
    errorFile.write(".I"+errorD+"\n")
    errorFile.write("===================================\n")

main()
