# file = input("Create a file: ")
# mode = input('''
# Mode: w, a, r.
# select one of them: 
#              ''')

# fhand = open(file, mode)
# words = input('''Enter your words: 
              
#               ''')
# fhand.write(words)
file = input("Enter name of file: ")
# with open(file) as ab:
#     text=ab.read()
#     print(text)

try:
    abd=open(file)
    for line in abd:
        print(line)
except FileNotFoundError:
    print("File not Found!!!")
