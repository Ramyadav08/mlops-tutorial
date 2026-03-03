class Chatbook:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        while True:
            user_input = input('''
Welcome to Chatbook!
1. Press 1 to Signup
2. Press 2 to Signin
3. Press 3 to Write a Post
4. Press 4 to Message
5. Press any other key to Exit

''')

            if user_input == "1":
                self.signup()
            elif user_input == "2":
                self.signin()
            elif user_input == "3":
                self.mypost()
            elif user_input == "4":
                self.message()
            else:
                print("Goodbye ")
                break

    def signup(self):
        self.username = input("Enter email: ")
        self.password = input("Set password: ")
        print("Registration successful ")

    def signin(self):
        if self.username == "" and self.password=="":
            print("Please signup first.")
            return

        uname = input("Enter username: ")
        pwd = input("Enter password: ")

        if self.username == uname and self.password == pwd:
            self.loggedin = True
            print("Login successful ")
        else:
            print("Invalid credentials ")

    def mypost(self):
        if self.loggedin:
            txt = input("Write your post: ")
            print(f"Post published: {txt}")
        else:
            print("Please login first.")

    def message(self):
        if self.loggedin:
            msg = input("Write your message: ")
            print(f"Message sent: {msg}")
        else:
            print("Please login first.")


obj = Chatbook()