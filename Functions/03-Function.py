def add(*x):
    print(sum(x))
    # s = 0
    # for i in x:
    #     s += i
    # print(s)

add(3,4,5)
add(5,6,7,4,54)
add(12,23,56,4,6,7,4)

def student(name,age,*course):
    print("Name :",name)
    print("Age :",age)
    print("Course :",course)

student('Ram',19,'Python')
student('Ram',19,'Python','C')
student('Ram',19,'Python','C','C++','ML')