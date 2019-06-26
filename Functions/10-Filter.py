# def even(num):
#     return num % 2 == 0

# print(even(5))

numbers = [i for i in range(1,51)]
# e = []
# for i in range(len(numbers)):
#     if even(numbers[i]):
#       e.append(numbers[i])
#
# print(e)
# e = list(filter(even, numbers))
# print(e)

e = list(filter(lambda x : x % 2 == 0, numbers))
print(e)