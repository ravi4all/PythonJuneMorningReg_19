import csv
# csv - comma seperated values
users = [
    {"name":"Ram","email":"ram@gmail.com","pwd":"1234"},
    {"name":"Raman","email":"raman@gmail.com","pwd":"4321"},
    {"name":"Shyam","email":"shyam@gmail.com","pwd":"4543"},
    {"name":"Aman","email":"aman@gmail.com","pwd":"8786"},
    {"name":"Mohit","email":"mohit@gmail.com","pwd":"2454"},
]

with open('data.csv','w',newline='') as file:
    writer = csv.writer(file)
    for user in users:
        writer.writerow(user.values())