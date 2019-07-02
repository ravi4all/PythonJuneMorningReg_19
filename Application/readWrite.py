import csv

def readData():
    pass

def writeData(user):
    with open('users.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user.values())