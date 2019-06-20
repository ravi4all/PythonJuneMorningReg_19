dataset = {
    "action" : ['superman','batman','antman','thor','hulk','baahubali',
                'avengers','kgf'],
    "comedy" : ["dhamaal",'golmaal'],
    "thriller" : ["lucy","the nun","the ring"],
    "horror" : ["the nun","the ring"],
    "biopic" : ["ms dhoni"]
    }

user_1 = {'superman','batman','antman','thor','hulk','baahubali','lucy',
          'dhamaal','ms dhoni','the ring','blade','x-men'}

user_2 = {'batman','thor','antman','baahubali','ms dhoni','avengers','golmaal',
          'the nun','hulk','kgf'}

intersection = user_1.intersection(user_2)
union = user_1.union(user_2)

j = len(intersection) / len(union)
print(round(j*100,2))
print("Sim Movies are",intersection)


#{"action":4,"comedy":3,"thriller":2,"horror":0,"biopic":1}

data = {'action':0,'comedy':0,'thriller':0,'horror':0,'biopic':0}

for movie in intersection:
    if movie in dataset["action"]:
        data['action'] += 1
    elif movie in dataset["comedy"]:
        data['comedy'] += 1
    elif movie in dataset["thriller"]:
        data['thriller'] += 1
    elif movie in dataset["horror"]:
        data['horror'] += 1
    elif movie in dataset["biopic"]:
        data['biopic'] += 1

print(data)













