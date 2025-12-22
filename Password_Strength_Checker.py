class password_checker:
    def __init__(self):
        self.password = ''
        self.score = 0
    
    def input(self):
        self.password = input("Enter a Password: ")
        
    def evaluations(self):
        pass

    def output(self):
        if self.score <= 3:
            print(f"Weak Password: {self.score}")
        elif self.score >= 4 or self.score <= 6:
            print(f"Medium Password: {self.score}")
        elif self.score >= 7 or self.score <= 9:
            print(f"Strong Password: {self.score}")
        elif self.score >= 10:
            print(f"Very strong password: {self.score}")