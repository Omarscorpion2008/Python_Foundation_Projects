import os
class Text_Cleaner:
    def __init__(self):
        with open('C:/Users/omara/OneDrive/Documents/Github/Python_Foundation_Projects/Text_File_Cleaner/old_text.txt', 'r', encoding='utf-8') as file:
            self.content = file.read()
            
txt_clean = Text_Cleaner()