class Bank:
    def __init__(self):
        self.database = {}
        self.dataloader()
        self.validation()
        self.data_updater()
    
    def dataloader(self):
        with open('Banking_System_With_Username_Password/database.csv','r', encoding='utf-8') as file:
            self.content = file.read()
            self.lines = self.content.split('\n')
            for line in self.lines:
                items = line.split(',')
                username = items[0]
                password = items[1]
                balance = int(items[2])
                self.database[username] = [password, balance]
    
    def validation(self):
        self.username = input("Provide your username: ")
        self.password = input("Provide your Password: ")    
        while True:
            if self.username in self.database.keys():
                if self.database[self.username][0] == self.password:
                    user_answer = input("Deposit (d) / Withdraw (w) / Balance Check (b) / exit (q): ").lower()
                    if user_answer == 'd':
                        self.deposit()
                    elif user_answer == 'w':
                        self.withdraw()
                    elif user_answer == 'b':
                        self.balance_check()
                    else:
                        break
                else:
                    print("Incorrect credentials, try again")
            else:
                answer = input("User not found, would you like to create an account? (y/n) : ").lower()
                if answer == 'y':
                    new_username = input("Enter your Username: ")
                    new_password = input("Enter your password: ")
                    new_balance = int(input("Enter your Balance: "))
                    self.database[new_username] = [new_password, new_balance]
                    print("Account added successfully")
                else:
                    print("Thank your for using the program")
                    break
    
    def deposit(self):
        user_answer = int(input("How much would you like to deposit into your account? : "))
        self.database[self.username][1] += user_answer
        
    def withdraw(self):
        user_answer = int(input("How much would you like withdraw from your account? : "))
        if self.database[self.username][1] - user_answer < 0:
            print("insufficient funds")
        else:
            self.database[self.username][1] -= user_answer
        
    def balance_check(self):
        print(f"Account Balance: {self.database[self.username][1]}")
    
    def data_updater(self):
        with open('Banking_System_With_Username_Password/database.csv','w', encoding='utf-8') as file:
            for key in self.database:
                line = str(key) + ',' + str(self.database[key][0]) + ',' + str(self.database[key][1]) + '\n'
                file.write(line)
    
Bank()