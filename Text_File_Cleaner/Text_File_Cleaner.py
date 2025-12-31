import os
class Text_Cleaner:
    def __init__(self):
        self.buffer = ''
        self.new_sentence = ''
        with open('C:/Users/omara/OneDrive/Documents/Github/Python_Foundation_Projects/Text_File_Cleaner/old_text.txt', 'r', encoding='utf-8') as file:
            self.content = file.read()
    
        Text_Cleaner.normalizer(self)

    def normalizer(self):
        for character in self.content:

            if character.isupper() and self.buffer == '':
                self.buffer = self.buffer + character
            elif character.isupper() and self.buffer[-1].isupper():
                self.buffer = self.buffer + character.lower()
            elif character.isupper() and self.buffer[-1].islower():
                self.buffer = self.buffer + character.lower()
            elif character.isupper() and not self.buffer[-1].isalpha():
                self.buffer = self.buffer + character


            if character.islower() and self.buffer == '':
                self.buffer = self.buffer + character.upper()
            elif character.islower() and self.buffer[-1].lower():
                self.buffer = self.buffer + character.lower()
            elif character.islower() and self.buffer[-1].isupper():
                self.buffer = self.buffer + character.lower()
            elif character.islower() and not self.buffer[-1].isalpha():
                self.buffer = self.buffer + character

            if character == ' ' and self.buffer[-1] in ",.?!'":
                self.buffer = self.buffer + character
            elif character == ' ' and self.buffer[-1] == ' ':
                continue
            elif character == ' ' and self.buffer[-1].isalpha():
                continue

            if character in "'":
                self.buffer = self.buffer + character

            if character in ",.?!":
                self.buffer = self.buffer + character + " "

        Text_Cleaner.output(self)    

    def output(self):
        print(self.buffer)

txt_clean = Text_Cleaner()
txt_clean.__init__()