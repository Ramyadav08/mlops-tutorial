class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.menu()
        
    def menu(self):
        user_input=input('''Welcome to chatbook! 
                         1.press 1 to singup
                         2. press 2 to singin
                         3. press 3 to write a post
                         4 press 4 to message 
                         5 press any other key to exit \n''')
        
        if user_input=="1":
            self.singup()
        elif user_input=="2":
            self.singin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()
            
    def singup(self):
        email=input("enter the email here: ")
        password=input("set the pass word: ")
        self.username=email
        self.password=password
        print("thank for registration!!!!")
        print("\n")
        self.menu()
        
    def singin(self):
        if self.username=="" and self.password=="":
            print("Please signup first by pressing 1")
            self.menu()
            
        else:
            uname=input("enter the username:")
            pwd=input("please enter the password:")
            if self.username!=uname and self.password!=pwd:
                print("Credentials are wrong,please fill the correct creds")
                self.singin()
            else:
                print("you logged in succesfully")
        
        
obj=chatbook()