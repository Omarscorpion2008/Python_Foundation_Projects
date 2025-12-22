class password_checker:
    def __init__(self):
        self.password = ''
        self.score = 0
    
    def input(self):
        self.password = input("Enter a Password: ")
        
    def evaluations(self):

        if len(self.password) < 12:
            self.score = 0
            return self.score
        elif len(self.password) >= 14:
            self.score = self.score + 4
            if len(self.password) > 14:
                bonus = (len(self.password) - 14) / 2
                self.score = self.score + bonus
        elif all(c.isspace() for c in self.password) or self.password == '':
            self.score = 0
        elif not any(c.isalpha() for c in self.password):
            self.score = min(self.score, 4)
        elif any(c.islower() for c in self.password):
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
        elif self.score >= 4 and self.score <= 6:
            print(f"Medium Password: {self.score}")
        elif self.score >= 7 and self.score <= 9:
            print(f"Strong Password: {self.score}")
        elif self.score >= 10:
            print(f"Very strong password: {self.score}")

pass_checker = password_checker()

pass_checker.input()
pass_checker.evaluations()
pass_checker.output()