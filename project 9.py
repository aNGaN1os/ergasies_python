#asking the user for input of the location of the file.
f = open(input("Please Give the Path of Your File: "), "r", encoding='utf-8')
TEXT = f.read()
f.close()
dict = {}
for i in TEXT:
    CurrChar = ord(i)
    if (CurrChar%2==1 and ((CurrChar>=65 and CurrChar<=90) or(CurrChar>=97 and CurrChar<=122))):
        if i in dict.keys():
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1


            
Allchars = 0
for i in dict:
    Allchars = Allchars + dict[i]
if (Allchars!=0):
    for i in dict:
        print(i,end = ': ')
        percentage = 100*dict[i]/Allchars
        if (percentage != int(percentage)):
            percentage = int(percentage) + 1
        for j in range(percentage):
            print("*",end = '')
        print()
else:
    print("Text has no ASCI character which has odd ASCI code!")
