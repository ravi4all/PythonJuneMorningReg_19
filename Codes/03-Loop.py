'''
*
**
***
****
*****
'''

for i in range(6):
    for j in range(i+1):
        print('*',end='')
    print()
'''
1
12
123
1234
12345
'''
for i in range(6):
    for j in range(i+1):
        print(j+1,end='')
    print()

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(10):
    for j in range(10-i):
        print(' ',end='')
    for k in range(2*i + 1):
        print('*',end='')
    print()
