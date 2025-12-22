class password_checker:
    def __init__(self):
        self.password = ''
        self.score = 0
    
    def input(self):
        self.password = input("Enter a Password: ")
        
    def evaluations(self):

        if len(self.password) < 12:
            self.score = 0
        elif len(self.password) >= 14:
            self.score = self.score + 4
            if len(self.password) > 14:
                bonus = (len(self.password) - 14) / 2
                self.score = self.score + bonus

        if not any(c.isalpha() for c in self.password):
            self.score = min(self.score, 4)
        elif all(c.isspace() for c in self.password) or self.password = '':
            self.score = 0
        
        if any(c.islower() for c in self.password):
            self.score = self.score + 2
        elif any(c.isupper() for c in self.password):
            self.score = self.score + 2
        elif any(c.isnumeric() for c in self.password):
            self.score = self.score + 2
        elif any(c in '!@#$%^&*.' for c in self.password):
            self.score = self.score + 3
    def output(self):

        if self.score <= 3:
            print(f"Weak Password: {self.score}")
        elif self.score >= 4 or self.score <= 6:
            print(f"Medium Password: {self.score}")
        elif self.score >= 7 or self.score <= 9:
            print(f"Strong Password: {self.score}")
        elif self.score >= 10:
            print(f"Very strong password: {self.score}")