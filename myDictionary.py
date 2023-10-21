# Dictionary as the collections in python  store values 
# in the form of Key and Value pairs. 
# The element consists of one pair of a key and a value separated by ':'
# We use curly braces {} for the same.
# Unlike lists there is no index in the dictionary. 
# The key is the index. i.e. myDict["age"] will return 30

myDict = {"name" : "John Walter", "age" : 35, "salary" : 35000}

print("His name is %s who is %d years old, he is a %s"% (myDict.get("name"), myDict.get("age"), myDict.get("designation", "Manager")))

d1 = myDict.copy
myDict.clear()
print("New dictionary elements", len(d1))
print(myDict)
# print(myDict["name"])
# print(myDict["age"])                          
# print(myDict["salary"])

# for k in myDict:
#     print('\t', k, '\t:', myDict[k])
# newKey = input("Enter the new key to be added: ")
# newValue = input("Enter the new value to be added: ")
# myDict.update({newKey : newValue})
# print(myDict)
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items()) # The output is the list having tuples containing the key and value