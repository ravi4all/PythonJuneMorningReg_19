from datetime import datetime
import webbrowser

print("Welcome".center(20,'*'))

helloIntent = ["hi","hello","hey","hello there","hi there"]
timeIntent = ["tell me time","time please","time","what's the time"]
dateIntent = ["tell me date","date please","date","what's the date","today's date"]
musicIntent = ["play music","start song","play song","start music"]


#Membership Operator - in, not in
chat = True
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = datetime.now().date()
        print(d.strftime('%d/%m/%y,%a'))
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime('%H:%M:%S,%p'))
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg in songIntent:
        pass
    elif msg == "bye":
        print("Bye,See you later...")
        chat = False
    else:
        print("I don't understand")
