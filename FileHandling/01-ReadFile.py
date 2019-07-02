# open file in read mode
file = open('file_1.txt','r')
# file = open('01-ReadFile.py','r')
# data = file.read()

# will read data line by line
# data = file.readline()

# will read till 10th character
# data = file.read(10)

# data = file.readlines()

file.seek(10)
data = file.read()
print(data)
file.close()