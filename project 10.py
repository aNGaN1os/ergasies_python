def Depth(x):
    maxDepth = 0
    if type(x) == type([]):
        for i in x:
            d = Depth(i)
            if d>maxDepth:
                maxDepth = d
    elif type(x) == type({}):
        for i in x.keys():
            d = Depth(x[i])
            if d>maxDepth:
                maxDepth = d

    return maxDepth+1



import json
#asking the user for input of the location of the file.
with open(input("Please Give the Path of Your File: ")) as f:
    data = f.read()

Dictionary = json.loads(data)




CurrDepth = 0
for i in Dictionary.keys():
    d = Depth(Dictionary[i])
    if d>CurrDepth:
        CurrDepth = d



print("Depth: ",CurrDepth)
