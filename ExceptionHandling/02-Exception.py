try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a + b
    d = a - b
    e = a / b
    f = a * b
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input, Please enter a digit from 0-9")
except BaseException as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)
    print(f)