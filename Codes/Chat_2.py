print("Welcome".center(20,'*'))

#Logical Operator - and, or, not
while True:
    msg = input("Enter your message : ")
    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hi there":
        print("Hello User")
    elif msg == "bye":
        print("Bye,See you later...")
        break
    else:
        print("I don't understand")
