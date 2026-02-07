import random
import string
class Shortener:
    def __init__(self):
        self.database = {}
        self.startup()
    
    def startup(self):
        print('-' * 47)
        print('- Shorten URL (s) | Expand URL (e) | exit (q) -')
        print('-' * 47)
        while True:
            user_input = input("which service do you prefer?: ").lower()
            if user_input == 's':
                self.shorten()
            elif user_input == 'e':
                self.expand()
            elif user_input == 'q':
                print("Thanks for using the program")
                break
            else:
                print("Provide valid input.")

    def shorten(self):
        user_input = input("Enter your URL: ")
        while True:
            random_number = random.randint(0,3000)
            random_character_chunk = random.sample(string.ascii_lowercase, k=3)
            random_character_chunk = ''.join(random_character_chunk)
            url_key = str(random_character_chunk) + str(random_number)
            if url_key not in self.database:
                self.database[url_key] = user_input
                return print(f"Your Short code: {url_key}")
            else:
                continue

    def expand(self):
        user_input = input("Enter your code: ")
        if user_input in self.database:
            extended_url = self.database[user_input]
            print(f"Your URL: {extended_url}")
        else:
            print("Code not found in database.")

Shortener()