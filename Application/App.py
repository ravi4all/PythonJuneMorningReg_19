from datetime import datetime

users = []
posts = []
def loginSuccess(email):
    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    """)
    ch = input("Enter your choice : ")
    todo = {
        "1" : post,
        "2" : viewProfile,
        "3" : updateProfile,
        "4" : deleteProfile
    }
    todo.get(ch)(email)

def post(email):
    p = input("Enter your post : ")
    date = datetime.now().date()
    userPost = {'post':p, 'date':date,'email':email}
    posts.append(userPost)

def viewProfile(email):
    pass

def updateProfile(email):
    pass

def deleteProfile(email):
    pass

def login():
    email = input("Enter Email : ")
    pwd = input("Enter Password : ")
    for user in users:
        if user['email'] == email and user['pwd'] == pwd:
            print("Login Success...")
            loginSuccess(email)
            break
    else:
        print("Login Failed...")

def register():
    name = input("Enter name : ")
    flag = True
    while flag:
        email = input("Enter email : ")
        if len(users) > 1:
            for i in range(len(users)):
                if users[i]['email'] == email:
                    print("EmailID Already Exist...")
                    break
            else:
                flag = False
        else:
            flag = False

    pwd = input("Enter pwd : ")
    user = {"name":name, "email":email,"pwd":pwd}
    users.append(user)
    for item in users:
        print(item)


def main():
    while True:
        print("""
        1. Register
        2. Login
        """)

        ch = input("Enter your choice : ")
        todo = {
            "1" : register,
            "2" : login
        }
        todo.get(ch)()

main()