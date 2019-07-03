# AssertionError
def atm():
    totalBal = 10000
    pin = input("Enter your PIN : ")
    assert (pin == "1234"), "Invalid PIN"
    print("Login Success")
    amount = int(input("Enter the amount : "))
    assert (amount < totalBal), "Insufficient Balance"
    totalBal -= amount
    print("Remaining Balance is", totalBal)

try:
    atm()
except AssertionError as err:
    print(err)
    atm()