import os
class Text_Cleaner:
    def start(self):
        self.buffer = ''
        self.content = open('C:/Users/omara/OneDrive/Documents/Github/Python_Foundation_Projects/Text_File_Cleaner/old_text.txt', 'r', encoding='utf-8')
        
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

            if character == ' ' and self.buffer[-1] in ".,?!'":
                self.buffer = self.buffer + character
            elif character == ' ' and ( self.buffer[-1].isupper() or self.buffer[-1].islower() ):
                self.buffer = self.buffer + character
            elif character == ' ' and self.buffer[-1] == ' ':
                continue

            if character in "'":
                self.buffer = self.buffer + character 
            if character in ".,?!" and self.buffer[-1] == ' ':
                self.buffer = self.buffer[:-1]
            if character in ".,?!" and self.buffer[-1] == character:
                self.buffer = self.buffer[:-1]   
            if character in ".,?!":
                self.buffer = self.buffer + character + " "
            if character == '.':
                self.buffer = self.buffer + character + "\n"

        Text_Cleaner.output(self)    

    def output(self):
        print(self.buffer)

txt_clean = Text_Cleaner()
txt_clean.start()