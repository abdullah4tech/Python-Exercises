'''
    Write a program to open any text file and read it line by line. 
    For each line, split the line into list of words using split 
    fucntion. For each word, check to see if the word is already 
    in the list. If the word is not in the list, add it to the list.
    When the program completes, sort and print the resulting words 
    in alphabetical order. 
'''
myList = []
fHand = open("romeo.txt")

#with open("romeo.txt") as fHand:
for line in fHand:
    words = line.split()
    for word in words:
        if word in myList: continue
        myList.append(word)
myList.sort()
print(myList)