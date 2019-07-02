# will create a new file if file do not exist
file = open('file_2.txt','w')

# data type can only be string
data = ["Hello world","Bye World"]
for item in data:
    file.write(item+'\n')
file.close()