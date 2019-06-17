from datetime import datetime
import webbrowser
import random,os

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
    elif msg in musicIntent:
        path = r"C:\Users\asus\Music"
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "show songs":
        path = r"C:\Users\asus\Music"
        os.chdir(path)
        songs = os.listdir()
        '''
        for song in songs:
            print(song)
        '''
        '''
        for i in range(len(songs)):
            print(i,songs[i])
        '''
        for i,song in enumerate(songs,start=1):
            print(i,song)

        index = int(input("Enter the song number : "))
        currentSong = songs[index - 1]
        os.startfile(currentSong)
    elif msg == "bye":
        print("Bye,See you later...")
        chat = False
    else:
        print("I don't understand")
