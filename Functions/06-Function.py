def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x * y
    z4 = x / y
    return z1,z2,z3,z4

# a = calc(4,5)
# print(a)

# Packing, Unpacking

# a,b,c,d = calc(2,4)
# a,b,*c = calc(2,4)

a,*b,c = calc(2,4)
print(a,b,c)