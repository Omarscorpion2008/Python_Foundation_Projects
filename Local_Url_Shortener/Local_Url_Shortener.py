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
            else:
                print("Provide valid input.")

    def shorten(self):
        user_input = input("Enter your URL: ")

    
    def expand(self):
        print("EXPAND DEF")
Shortener()