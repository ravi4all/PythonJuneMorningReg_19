num = int(input("Enter a number : "))

'''
flag = True
for n in range(2,int(num/2)):
    if num % n == 0:
        # print("Not Prime")
        flag = True
        break
    else:
        # print("Prime")
        flag = False

if flag:
    print("Not Prime Number")
else:
    print("Prime Number")
'''

for n in range(2, num):
    if num % n == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")