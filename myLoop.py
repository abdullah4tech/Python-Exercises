# nCtr = 5
# while(nCtr > 0):
#     print(nCtr, 'NIIT - learning never stops!')
#     nCtr -= 1
# print('*******************')
# nCtr = 1
# while(nCtr <= 5):
#     print(nCtr, 'NIIT - learning never stops!')
#     nCtr += 1

# n = 2
# while (n <= 10):
#     if(n % 2 == 0):
#         print(n, end = ' ')
#     n += 1

# while True:
#     line = input('Enter something >>> ')
#     if(line == 'done'):
#         break
#     print(line)
# print("Done!!!")


# while True:
#     line = input('Enter something >>> ')
#     if(line[0] == '#'):
#         continue
#     if(line == 'done'):
#         break
#     print(line)
# print("Done!!!")

Total = 0
iMax = 0 
iMin = 0

myValList = [45, 34, 10, 67, 105, 78, 99]
for sum in myValList:
    Total += sum
print('The sum of the values in list is: ', Total)

for sum in myValList:
    if(iMin == 0 or iMin > sum):
        iMin = sum
print('The min of the values in list is: ', iMin)


for sum in myValList:
    if(iMax == 0 or iMax < sum):
        iMax = sum
print('The max of the values in list is: ', iMax)

