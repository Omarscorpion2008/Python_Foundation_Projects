class Word_Frequency:
    def __init__(self):
        self.user_input = ""
        self.sentence = ""
        self.dictionary = {}

    def start(self):
        self.user_input = input("Enter the sentence: ")
        self.special_character_remover()
    
    def special_character_remover(self):
        for character in self.user_input:
            if character in "!@#$%^&*,.":
                self.sentence = self.sentence + " "
            else:
                self.sentence = self.sentence + character.lower()
        

            
word = Word_Frequency()
word.start()