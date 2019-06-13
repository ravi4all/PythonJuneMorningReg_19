print("Welcome".center(20,'*'))

helloIntent = ["hi","hello","hey","hello there","hi there"]

while True:
    msg = input("Enter your message : ")
    for i in range(len(helloIntent)):
        if helloIntent[i] == msg:
            print("Hello User")
    elif msg == "bye":
        print("Bye,See you later...")
        break
    else:
        print("I don't understand")
