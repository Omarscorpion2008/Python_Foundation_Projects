class Calculator:

    def __init__(self):
        self.question = ''
        self.numbers_string = []
        self.numbers_float = []
        self.spaces = []
        self.operations = []
        self.result = 0
        self.buffer = ''
    
    def input(self):
        self.question = input("Enter your Expression: ")
        return self.question

    def parse(self):
        prev_char = ''

        for character in self.question:
        
            if character.isnumeric() or character == '.':
                self.buffer += character

            elif character == '-' and (prev_char == '' or prev_char in '+-*/ '):
                self.buffer += character

            elif character in '+-*/':
                if self.buffer != '':
                    self.numbers_string.append(self.buffer)
                    self.buffer = ''
                self.operations.append(character)

            elif character == ' ':
                if self.buffer != '':
                    self.numbers_string.append(self.buffer)
                    self.buffer = ''

            prev_char = character

        if self.buffer != '':
            self.numbers_string.append(self.buffer)
        self.buffer = ''
                    
    def evaluation(self):
        self.numbers_float = [float(number) for number in self.numbers_string]
        self.result = self.numbers_float[0]

        for index in range(len(self.operations)):
                
            if self.operations[index] == '+':
                self.result += self.numbers_float[index + 1]

            elif self.operations[index] == '-':
                self.result -= self.numbers_float[index + 1]

            elif self.operations[index] == '*':
                self.result *= self.numbers_float[index + 1]

            elif self.operations[index] == '/':
                self.result /= self.numbers_float[index + 1]

    def output(self):
        print(f"Your total value: {self.result:.2f}")
        self.question = ''
        self.numbers_string = []
        self.numbers_float = []
        self.spaces = []
        self.operations = []
        self.result = 0
        self.buffer = ''

calc = Calculator()

while True:
    try:
        if calc.input() != '':
            calc.parse()
            calc.evaluation()
            calc.output()
    except ZeroDivisionError:
        print("Cannot divide by zero")