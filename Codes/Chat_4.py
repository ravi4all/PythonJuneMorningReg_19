print("Welcome".center(20,'*'))

helloIntent = ["hi","hello","hey","hello there","hi there"]

#Membership Operator - in, not in

while True:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg == "bye":
        print("Bye,See you later...")
        break
    else:
        print("I don't understand")
