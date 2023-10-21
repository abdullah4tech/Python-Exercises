import json
myData = '''
	[
	{"name" : "Success", "city" : "Freetown", "mobile" : 11223344},
	{"name" : "Esther", "city" : "Bo", "mobile" : 112345678},
	{"name" : "Ishmail", "city" : "Western", "mobile" : 44444444},
	{"name" : "Abdullah", "city" : "Waterloo", "mobile" : 9999999},
	{"name" : "Prosper", "city" : "Kenema", "mobile" : 112112112}
	]'''
myJSON_Data = json.loads(myData)
print("\n Student Count:\t\t", len(myJSON_Data))
print("-"*35)
for s in myJSON_Data:
    print("\tName:\t\t", s["name"])
    print("\tCity:\t\t", s["city"])
    print("\tContact:\t", s["mobile"])
    print("-"*35)
print("\nDONE!!!")