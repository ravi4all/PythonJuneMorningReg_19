import io
try:
    file = open('file_1.txt')
    data = file.read()
    print(data)

    # text = "This is some dummy data"
    # file.write(text)
except FileNotFoundError:
    print("File Not Found")
except io.UnsupportedOperation:
    print("File is being open in different mode...")
finally:
    print("This code will always execute")
    file.close()