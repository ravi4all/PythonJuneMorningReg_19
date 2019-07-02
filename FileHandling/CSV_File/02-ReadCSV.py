import csv

users = []

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        user = {"name":row[0],"email":row[1],"pwd":row[2]}
        users.append(user)

print(users)