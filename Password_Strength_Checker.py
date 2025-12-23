class password_checker:
    def __init__(self):
        self.password = ''
        self.buffer = ''
        self.sub = 0
        self.score = 0.0
    
    def input(self):
        self.password = input("Enter a Password: ")

    def evaluations(self):

        self.score = 0.0
        self.buffer = ''
        self.sub = 0

        if all(c.isspace() for c in self.password) or self.password == '':
            self.score = 0
            return self.score

        if len(self.password) < 14:
            self.score = 0
            return self.score

        if len(self.password) >= 14:
            self.score = self.score + 4
            bonus = (len(self.password) - 14) / 2
            bonus = min(bonus, 5)
            self.score = self.score + bonus
        
        if any(c.islower() for c in self.password):
            self.score = self.score + 2
        
        if any(c.isupper() for c in self.password):
            self.score = self.score + 2
        
        if any(c.isnumeric() for c in self.password):
            self.score = self.score + 2
        
        if any(c in '!@#$%^&*.' for c in self.password):
            self.score = self.score + 3

        if not any(c.isalpha() for c in self.password):
            self.score = min(self.score, 4)

        for character in self.password:
    
            if self.buffer == '' or character == self.buffer[-1]:
                self.buffer = self.buffer + character 
            else:
                if len(self.buffer) > 2:
                    self.sub = min(len(self.buffer), 3)
                    self.score = self.score - self.sub
                    self.buffer = character
        if len(self.buffer) > 2:
            self.sub = min(len(self.buffer), 3)
            self.score = self.score - self.sub
            self.buffer = character            

    def output(self):
        self.score = self.score / 2
        
        if self.score <= 2:
            print(f"Weak Password: {self.score}")
        elif self.score >= 2.5 and self.score <= 5:
            print(f"Medium Password: {self.score}")
        elif self.score >= 6.5 and self.score <= 10:
            print(f"Strong Password: {self.score}")
        elif self.score > 10:
            print(f"Very strong password: {self.score}")

pass_checker = password_checker()

print("-" * 30)
print("- Password Strength Checker -")
print("-" * 30)


while True:
    pass_checker.input()
    pass_checker.evaluations()
    pass_checker.output()