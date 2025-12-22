class password_checker:
    def __init__(self):
        self.password = ''
        self.buffer = ''
        self.score = 0.0
    
    def input(self):
        self.password = input("Enter a Password: ")

    def evaluations(self):

        if all(c.isspace() for c in self.password) or self.password == '':
            self.score = 0
            return self.score

        if len(self.password) < 14:
            self.score = 0
            return self.score

        if len(self.password) >= 14:
            self.score = self.score + 4
            if len(self.password) > 14:
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

    def output(self):

        if self.score <= 4:
            print(f"Weak Password: {self.score}")
        elif self.score >= 5 and self.score <= 10:
            print(f"Medium Password: {self.score}")
        elif self.score >= 11 and self.score <= 20:
            print(f"Strong Password: {self.score}")
        elif self.score > 20:
            print(f"Very strong password: {self.score}")

pass_checker = password_checker()

pass_checker.input()
pass_checker.evaluations()
pass_checker.output()