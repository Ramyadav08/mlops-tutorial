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

    def post(self):
        if self.loggedin:
            txt = input("Write your post: ")
            print("User post published:", txt)
        else:
            print("Login first.")


class Admin(User):

    def post(self):   # Method Overriding
        if self.loggedin:
            txt = input("Write admin announcement: ")
            print("Admin announcement published:", txt)
        else:
            print("Admin must login first.")



u = User()
a = Admin()

print("\n--- USER ---")
u.signup()
u.signin()
u.post()

print("\n--- ADMIN ---")
a.signup()
a.signin()
a.post()