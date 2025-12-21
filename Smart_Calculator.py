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
        question = input("Enter your Expression: ")

    def parse(self, question, operations, numbers_string):

        for character in question:

            if question[0] and character == '-':
                buffer = buffer + str(character)
        
            elif character.isnumeric()  or character == '.':
                buffer = buffer + str(character)
        
            elif character in '+-*/':
                if buffer != '':
                    numbers_string.append(buffer)
                    buffer = ''
                operations.append(character)
        
            elif character == ' ':
                if buffer != '':
                    numbers_string.append(buffer)
                    buffer = ''
        numbers_string.append(buffer)

    def evalutaion(self, numbers_strings, operations, result):
        numbers_floats = [float(number) for number in numbers_strings]

        for index in range(len(operations)):

                if operations[index] == '+':

                    if index > 0:
                        result = result + numbers_floats[index + 1]
                    elif index == 0:
                        result = numbers_floats[index] + numbers_floats[index + 1]

                elif operations[index] == '-':

                    if index > 0:
                        result = result - numbers_floats[index + 1]
                    elif index == 0:
                        result = numbers_floats[index] - numbers_floats[index + 1]

                elif operations[index] == '*':

                    if index > 0:
                        result = result * numbers_floats[index + 1]
                    elif index == 0:
                        result =  numbers_floats[index] * numbers_floats[index + 1]

                elif operations[index] == '/':

                    if index > 0:
                        result = result / numbers_floats[index + 1]
                    elif index == 0:
                        result = numbers_floats[index] / numbers_floats[index + 1]

    def output(self, result):
        print(f"Your total value: {result:.2f}")