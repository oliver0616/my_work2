
'''file = open("pos.bib","r")
for each in file:
    each = each.replace("\n","")
    print(each+"<br>")'''
#==============================================================
file = open("pos.bib","r")
outputFile = open("pos_result.bib","w")
inputFile = file.read()

result = []
mem = 0

splitString = inputFile.split("@")
for each in splitString[1:]:
    storeLine=""
    year=""
    author=""
    title=""
    key=""
    splitLine = each.split("\n")
    for count, line in enumerate(splitLine):
        #take out original key
        if count == 0:
            for number, word in enumerate(line):
                if word == "{":
                    mem = number
            storeLine= storeLine +"@"+line[:mem] +"{ \n"
        #take out category
        elif "-TIT" in line:
            ""
        #fatch author last name
        elif "author" in line.lower():
            storeLine= storeLine + line + "\n"
            splitAuthor = line.split("=")
            author = splitAuthor[1].replace("{","")
            author = author.replace("}","")
            author = author.replace(",","")
            author = author.strip()
            authorS = author.split(" ")
            author = authorS[0].lower()
        elif "year" in line.lower():
            storeLine= storeLine + line + "\n"
            splitYear = line.split("=")
            year = splitYear[1].replace("{","")
            year = year.replace("}","")
            year = year.replace(",","")
            year = year.strip()
        elif "title" in line.lower():
            storeLine= storeLine + line + "\n"
            splitTitle = line.split("=")
            title = splitTitle[1].replace("{","")
            title = title.replace("}","")
            title = title.replace(",","")
            title = title.replace(" ","-")
            title = title.lower()
        else:
            storeLine= storeLine + line + "\n"
    if year=="" or author=="" or title=="":
        print("There is error key")
        print(each)
        print("====================================")
    key = year+"-"+author+"-"+title
    final=""
    for count , line in enumerate(storeLine.splitlines()):
        if count == 0:
            final = final + line.strip() + key +"\n"
        else:
            final= final + line+"\n"
    result.append(final)

for each in result:
    outputFile.write(each)
outputFile.close()
            
        
