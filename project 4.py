def Last2Words(x):
    i=-1
    wordNum=1
    while (wordNum!=3):
        if (x[i]==" " and wordNum==1):
            wordNum=2
        elif (x[i]==" " and wordNum==2):
            wordNum=3
        i-=1
    return x[i+2:]



def First2Words(x):
    i=0
    wordNum=1
    while (wordNum!=3):
        if (x[i]==" " and wordNum==1):
            wordNum=2
        elif (x[i]==" " and wordNum==2):
            wordNum=3
        i+=1
    return x[:i-1]



def LastWord(x):
    i=-1
    while (x[i]!=" "):
        i-=1
    return x[i+1:]



#asking the user for input of the location of the file.
f = open(input("Please Give the Path of Your File: "), "r", encoding='utf-8')
TEXT = f.read()
f.close()
WordList=[]
point=0
currWord=""

while (point+1<=len(TEXT)):
    if (TEXT[point]!=" "):
        currWord+=TEXT[point]
    else:
        WordList.append(currWord)
        currWord=""
    point+=1

if (currWord!=""):
    WordList.append(currWord)
    currWord=""

ThreeWordList=[]
for i in range(len(WordList)-2):
    ThreeWordList.append(WordList[i]+" "+WordList[i+1]+" "+WordList[i+2])

import random
random.shuffle(ThreeWordList)



#proceeds to make the new text.
NewText=ThreeWordList[0]
wordCount=3
stop=False

while (wordCount<200 and stop==False):
    i=0
    Found=False
    while (i<=len(ThreeWordList)-1 and Found==False):
        if ( First2Words(ThreeWordList[i]) == Last2Words(NewText) ) :
            Found=True
            NewText = NewText + " " + LastWord(ThreeWordList[i])
            wordCount=wordCount+1
        else:
            i+=1
    if (Found==False):
        stop=True

print(NewText)
