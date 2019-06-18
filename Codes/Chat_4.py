print("Welcome".center(20,'*'))

helloIntent = ["hi","hello","hey","hello there","hi there"]

#Membership Operator - in, not in
chat = True
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg == "bye":
        print("Bye,See you later...")
        chat = False
    else:
        print("I don't understand")
