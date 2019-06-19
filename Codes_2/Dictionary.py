'''
data = [
    {'name': 'Ram', 'age': 30, 'sal': 34000, 'dept': 'IT'},
    {'name': 'Shyam', 'age': 34, 'sal': 23000, 'dept': 'IT'},
    {'name': 'Aman', 'age': 29, 'sal': 37000, 'dept': 'HR'},
    {'name': 'Gopal', 'age': 26, 'sal': 20000, 'dept': 'HR'},
    {'name': 'Mohit', 'age': 38, 'sal': 40000, 'dept': 'Sales'},
    {'name': 'Sumit', 'age': 31, 'sal': 37000, 'dept': 'Sales'},
    ]

for i in range(len(data)):
    if data[i]['age'] >= 30 and data[i]['dept'] == 'IT':
        print(data[i]['name'], data[i]['age'], data[i]['dept'])

'''

data = {
    "names" : ["Rohit","Dhawan","Kohli","Jadhav","Dhoni","Jadeja"],
    "scores" : [100,90,120,56,76,34],
    "strike_rate" : [102.2,110.4,150.0,98.6,100.7,87]
    }

for i in range(len(data['names'])):
    if data["scores"][i] > 70:
        print(data["names"][i], data["scores"][i], data["strike_rate"][i])








