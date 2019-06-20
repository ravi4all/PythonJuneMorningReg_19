dataset = {
    "action" : ['superman','batman','antman','thor','hulk','baahubali',
                'avengers','kgf','blade','x-men'],
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

data = {}
for key in dataset:
    data[key] = 0

for movie in intersection:
    for key in dataset:
        if movie in dataset[key]:
            data[key] += 1
print(data)

items = data.items()
category = max(items, key=lambda i : i[1])

for movie in dataset[category[0]]:
    if movie not in user_2:
        print("Recommended",movie)









