## Declaration part 
nCtr = 0
nSum = 0

## Asking user for name of FILE
num = input("Enter the file name: ")
fhand = open(num, "r")
#result = fhand.read()

# Open the loop
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        l1 = line.split()
        nCtr = nCtr + 1
        nSum = nSum + float(l1[1])
print("The Average spam confidence: ", (nSum/nCtr))