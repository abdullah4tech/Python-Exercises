myList = []
while(True):
    resp = input("Enter the number: ")
    if (resp == 'done'): 
        break
    myList.append(int(resp))
print('The maximum: ',max(myList),'\nThe minimum: ',min(myList))
