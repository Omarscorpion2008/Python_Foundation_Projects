class Bank:
    def __init__(self):
        self.database = {}
        self.dataloader()
        self.main_menu()
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
    
    def main_menu(self):
            print('-' * 30)
            print("   -   Sign in window   - ")
            print('-' * 30)
            self.username = input("Please provide your username: ")
            self.password = input("Please provide your password: ")
            while True:
                if self.username == '' and self.password == '':
                    print("Thanks for using the program")
                    break
                
                if self.username in self.database.keys():
                    if self.password == self.database[self.username][0]:
                        self.services()
                        break
                    elif self.password != self.database[self.username][0]:
                        print("Incorrect Credentials")
                        break
                else:
                    user_answer = input("account doesn't exist, Would you like to create a new account (y/n): ").lower()
                    if user_answer == 'y':
                        self.create_account()
                    else:
                        print("Thanks for using the program")
                        break
                
    
    def create_account(self):
        while True:
            new_username = input("Provide your username: ")
            new_password = input("Provide your password: ")
            new_balance = int(input("Provide your balance: "))
            if new_balance >= 0 and new_username not in self.database.keys():
                self.database[new_username] = [new_password, new_balance]
                print("Account Created successfully.")
                break
            else:
                print("Please provide valid input.")
            
    def services(self):
        while True:
            print("Choose a service :")
            print("Check balance (b)")
            print("Deposit (d)")
            print("Withdraw (w)")
            answer = input().lower()
            if answer == 'b':
                self.balance_check()
            elif answer == 'd':
                self.deposit()
            elif answer == 'w':
                self.withdraw()
            elif answer == '':
                print("Logging out")
                return
            else:
                print("Provide valid input.")
    
    def deposit(self):
        while True:
            try:
                user_answer = int(input("How much would you like to deposit into your account? : "))
                self.database[self.username][1] += user_answer
                break
            except ValueError:
                print("Provide valid input")
                
    def withdraw(self):
        while True:
            try:
                user_answer = int(input("How much would you like withdraw from your account? : "))
                if self.database[self.username][1] - user_answer < 0:
                    print("insufficient funds")
                else:
                    self.database[self.username][1] -= user_answer
                    break
            except ValueError:
                print("Provide valid Input.")
            
    def balance_check(self):
        print(f"Account Balance: {self.database[self.username][1]}")
    
    def data_updater(self):
        with open('Banking_System_With_Username_Password/database.csv','w', encoding='utf-8') as file:
            for key in self.database:
                line = str(key) + ',' + str(self.database[key][0]) + ',' + str(self.database[key][1]) + '\n'
                file.write(line)
    
Bank()