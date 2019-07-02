file = open('Football.png','rb')
data = file.read()
# print(data)
file.close()

file = open('Football_2.png','wb')
file.write(data)
file.close()