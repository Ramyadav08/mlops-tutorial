class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False

    def signup(self):
        self.username = input("Enter email: ")
        self.password = input("Set password: ")
        print("Registration successful ")

    def signin(self):
        uname = input("Enter username: ")
        pwd = input("Enter password: ")

        if self.username == uname and self.password == pwd:
            self.loggedin = True
            print("Login successful ")
        else:
            print("Invalid credentials ")


class Chatbook(User):   # Inheriting from User

    def menu(self):
        while True:
            user_input = input("""
1. Signup
2. Signin
3. Post
4. Exit
""")

            if user_input == "1":
                self.signup()
            elif user_input == "2":
                self.signin()
            elif user_input == "3":
                self.post()
            else:
                break

    def post(self):
        if self.loggedin:
            txt = input("Write your post: ")
            print("Post published:", txt)
        else:
            print("Login first.")


obj = Chatbook()
obj.menu()