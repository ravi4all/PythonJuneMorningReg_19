def temp_conv(cel):
    return 9/5 * cel + 32

# f = temp_conv(34.5)
# print(f)

t = [34.5,33.5,36.7,40.3,42.1]
# temp_conv(t)

# x = []
# for temp in t:
#     f = temp_conv(temp)
#     x.append(f)
#
# print(x)

f = list(map(temp_conv, t))
print(f)

# def myMap(func, iter):
#     data = []
#     for i in range(len(iter)):
#         data.append(func(iter[i]))
#     return data
#
# data = myMap(temp_conv, t)
# print(data)
