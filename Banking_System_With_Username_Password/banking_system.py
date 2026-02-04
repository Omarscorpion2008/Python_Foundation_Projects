class Bank:
    def __init__(self):
        self.database = {}
        self.dataloader()
    
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
    
        
            
Bank()