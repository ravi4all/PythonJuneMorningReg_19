try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a + b
    print(c)
    d = a - b
    print(d)
    e = a / b
    print(e)
    f = a * b
    print(f)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input, Please enter a digit from 0-9")
except BaseException as ex:
    print(ex)