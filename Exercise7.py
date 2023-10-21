# myDict = []
# f = open("romeo.txt")
# for nCtr in f:
#     if 
myDictionary = {}
myList = []
myFullList = []
fHand = open("romeo.txt")
fHand1 = open("romeo.txt")

for line in fHand:
    words = line.split()
    for word in words:
        if word in myList: continue
        myList.append(word)

for line in fHand1:
    words = line.split()
    for word in words:
        myFullList.append(word)

for word in myList:
    ctr = 0
    for word1 in myFullList:
        if word == word1:
            ctr+=1
    myDictionary.update({word: ctr})
    
print(myDictionary)