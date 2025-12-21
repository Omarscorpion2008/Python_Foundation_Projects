class Calculator:

    def __init__(self):
        self.question = ''
        self.numbers = []
        self.spaces = []
        self.operations = []
        self.result = 0
        self.buffer = ''
    
    def input(self):
        question = input("Enter your Expression: ")

    def parse(self, question, operations, numbers):

        for character in question:

            if question[0] and character == '-':
                buffer = buffer + str(character)
        
            elif character.isnumeric()  or character == '.':
                buffer = buffer + str(character)
        
            elif character in '+-*/':
                if buffer != '':
                    numbers.append(buffer)
                    buffer = ''
                operations.append(character)
        
            elif character == ' ':
                if buffer != '':
                    numbers.append(buffer)
                    buffer = ''
        numbers.append(buffer)

    def evalutaion(self):
        pass

    def output(self):
        pass