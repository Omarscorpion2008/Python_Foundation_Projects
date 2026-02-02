class Formatter:
    def __init__(self):
        self.text = ''
        self.new_text = ''
        self.startup()
        
    def startup(self):
        self.text = input("Input your text: ")
        while True:
            try:
                user_input = input("What service would you like ?\nUppercase ?(u)\nLowercase(l)\nTitle-case (t)\nRemove punctuation? (r)\n,Save text(s):").lower()
                if user_input == 'u':
                    self.uppercase()
                elif user_input == 'l':
                    self.lowercase()
                elif user_input == 't':
                    self.titlecase()
                elif user_input == 'r':
                    self.rmv_punc()
                elif user_input == 's':
                    self.save_file()
            except ValueError:
                print("Please provide valid input.")
    
    def uppercase(self):
        self.new_text = self.text.upper()
        print(self.new_text)
        
    def lowercase(self):
        self.new_text = self.text.lower()
        print(self.new_text)
    
    def titlecase(self):
        self.new_text = self.text.title()
        print(self.new_text)
    
    def rmv_punc(self):
        self.new_text = ''
        for character in self.text:
            if character in ['.',',','?','!','(',')','[',']','/','-','_']:
                continue
            else:
                self.new_text = self.new_text + character
        print(self.new_text)
    
    def save_file(self):
        with open ('Text_Formatter_Tool/texts.txt','a+', encoding='utf-8') as file:
            file.write(self.new_text + '\n')
        
Formatter()