class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
        
    
    def menu(self):
        user_input = input(""""How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to Signin
                           3. Press 3 to write  a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit 
                           """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email = input('Enter your email: ')
        pw = input('Enter your password: ')
        self.username = email
        self.password = pw     
        print(f"Hi {email}, You have signed up successfully")
        print('/n')
        self.menu()
        
    def signin(self):
        if self.username == "" and self.password == '':
            print("Please Signup first by pressing 1 on the main menu")
            
        else:
            uname = input("Enter your email/username here: ")
            pwd = input("Enter your password: ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successful;y !! ")
            else:
                print("Please input correct details! ")
                
            print("/n")
            self.menu()
                
            
        
            
obj = chatbook()
        
        
        

        
        