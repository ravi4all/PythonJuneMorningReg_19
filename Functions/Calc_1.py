def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y if x > y else y - x
    print("Diff is",z)

def div(x,y):
    if y == 0:
        pass
    else:
        z = x / y
        print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")