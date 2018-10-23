'''inputFile = open("out.txt","r")
outputFile = open("output.txt","w")

for each in inputFile:
    each = each.replace("-",":")
    outputFile.write(each)
outputFile.close()'''
#===============================================================
#li=[]
inputF = open("in.txt","r")
outputF = open("input.txt","w")

for each in inputF:
    each = each.strip()
    outputF.write(each)
    outputF.write("\n")
    #li.append(each)
outputF.close()
#li.sort()
'''for each in li:
    outputF.write(each)
    outputF.write("\n")
outputF.close()'''
    
