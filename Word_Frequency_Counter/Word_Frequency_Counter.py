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
        self.parsing_counting()
        
    def parsing_counting(self):
        self.new_sentence = self.sentence.split(' ')
        
        for word in self.new_sentence:
            if word:
                self.dictionary[word] = self.dictionary.get(word, 0) + 1

        for item in self.dictionary:
            print(f"{item}: {self.dictionary.get(item)}")
        
word = Word_Frequency()
word.start()