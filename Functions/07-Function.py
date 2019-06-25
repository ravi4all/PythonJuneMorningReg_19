def outer():
    x = 12
    def add():
        y = 11
        z = x + y
        return z
    def sub():
        y = 15
        z = x - y
        return z
    # print(add())
    # print(sub())
    return add,sub

# print(outer()) it will print none because outer is not returning anything

z = outer()
print(z[0]())
print(z[1]())
