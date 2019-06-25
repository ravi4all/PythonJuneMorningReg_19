def add(x,y):
    print("Inside Add")
    z = x + y
    # print("Sum is",z)
    return z

def sub(x,y):
    print("Inside Sub")
    z = x - y if x > y else y - x
    # print("Diff is",z)
    return z

def div(x,y):
    print("Inside Div")
    if y == 0:
        pass
    else:
        z = x / y
        # print("Div is",z)
        return z

def mul(x,y):
    print("Inside Mul")
    z = x * y
    # print("Mul is",z)
    return z

def errorHandler(*args):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

operations = {"1" : add,
              "2" : sub,
              "3" : div,
              "4" : mul}

# print(operations[ch](num_1, num_2))
print(operations.get(ch, errorHandler)(num_1, num_2))






