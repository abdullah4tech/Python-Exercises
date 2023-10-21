import json

fhand = open("xyz.json", "r")
myData = fhand.read()
#print(mydata)
myJSON_Data = json.loads(myData)
print("\n Student Count:\t\t", len(myJSON_Data))
print("-"*35)
for s in myJSON_Data:
    print("\tName:\t\t", s["name"])
    print("\tCity:\t\t", s["city"])
    print("\tContact:\t", s["mobile"])
    print("-"*35)
print("\nDONE!!!")
