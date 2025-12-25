import random
from unittest import skip
from urllib.parse import ParseResultBytes
## add an option to show either it's odd or even
class Guessing_games:
    def __init__(self):
        self.high_score = 0
        self.current_score = 0
        self.attempts = 0
        self.target_number = 0
        self.guess = 0
        self.difficulty = ''
        self.replay = ''
        
    def get_user_input(self):
        self.attempts = 0
        self.current_score = 0  
        self.difficulty = input("Choose the difficulty (e: easy | m: medium | h: hard | q: quit): ")
        Guessing_games.difficulty_setter(self)
    
    def difficulty_setter(self):
        if self.difficulty != 'q':
            if self.difficulty == 'e':
                self.target_number = random.randint(0, 20)
                Guessing_games.level_easy(self)
            elif self.difficulty == 'm':
                self.target_number = random.randint(0, 100)
                Guessing_games.level_medium(self)
            elif self.difficulty == 'h':
               self.target_number = random.randint(0, 300)
               Guessing_games.level_hard(self)
        elif self.difficulty == 'q':
                return "Thanks for using the game."
            
    def helper(self):
            if self.attempts == 3:
                self.helper_start = input("\n Would you like to know whether the number is an odd or an even? [ score deduction will happen ] (y/n): ")
                if self.helper_start.lower() == 'y':
                    if self.target_number % 2 == 1:
                        print("\n The number is odd")
                        if self.difficulty == 'e':
                            self.current_score = self.current_score - 3
                            self.level_easy()
                        elif self.difficulty == 'm':
                            self.current_score = self.current_score - 2
                            self.level_medium()
                        elif self.difficulty == 'h':
                            self.current_score = self.current_score - 1
                            self.level_hard()
                    elif self.target_number % 2 == 0:
                        print("\n The number is even")
                        if self.difficulty == 'e':
                            self.current_score = self.current_score - 3
                            self.level_easy()
                        elif self.difficulty == 'm':
                            self.current_score = self.current_score - 2
                            self.level_medium()
                        elif self.difficulty == 'h':
                            self.current_score = self.current_score - 1
                            self.level_hard()
                else:
                    print("\n Alright I guess :(")
                    if self.difficulty == 'e':
                        self.level_easy()
                    elif self.difficulty == 'm':
                        self.level_medium()
                    elif self.difficulty == 'h':
                        self.level_hard()
            else:
                if self.difficulty == 'e':
                    self.level_easy()
                elif self.difficulty == 'm':
                    self.level_medium()
                elif self.difficulty == 'h':
                    self.level_hard()
    
    def level_easy(self):
        try:
            while self.attempts < 5 or self.guess != self.target_number:  
                self.guess = int(input("\n Enter your guess: "))
                if self.guess > self.target_number:
                    print(f"\n Wrong, guess lower")
                    self.attempts = self.attempts + 1
                    Guessing_games.helper(self)
                elif self.guess < self.target_number:
                    print(f"\n Wrong, guess higher")
                    self.attempts = self.attempts + 1
                    Guessing_games.helper(self)
                elif self.guess == self.target_number:
                    print(f"\n Correct! {self.target_number} was indeed the number!") 
                    if self.attempts == 0:
                        self.current_score = self.current_score + 6
                    elif self.attempts == 1:
                        self.current_score = self.current_score + 5
                    elif self.attempts == 2:
                        self.current_score = self.current_score + 4
                    elif self.attempts == 3:
                        self.current_score = self.current_score + 3
                    elif self.attempts == 4:
                        self.current_score = self.current_score + 2
                    elif self.attempts == 5:
                        self.current_score = self.current_score + 1
                    if self.current_score > self.high_score:
                        self.high_score = self.current_score
                    Guessing_games.output(self)
                        
        except (TypeError, ValueError):
            print("Please provide valid input.")
                            
        
    
    def level_medium(self):
        try:
            while self.attempts < 5 or self.guess != self.target_number:  
                self.guess = int(input("\n Enter your guess: "))
                if self.guess > self.target_number:
                    print(f"\n Wrong, guess lower")
                    self.attempts = self.attempts + 1
                    Guessing_games.helper(self)
                elif self.guess < self.target_number:
                    print(f"\n Wrong, guess higher")
                    self.attempts = self.attempts + 1
                    Guessing_games.helper(self)
                elif self.guess == self.target_number:
                    print(f"\n Correct! {self.target_number} was indeed the number!") 
                    if self.attempts == 0:
                        self.current_score = self.current_score + 10
                    elif self.attempts == 1:
                        self.current_score = self.current_score + 8
                    elif self.attempts == 2:
                        self.current_score = self.current_score + 7
                    elif self.attempts == 3:
                        self.current_score = self.current_score + 6
                    elif self.attempts == 4:
                        self.current_score = self.current_score + 5
                    elif self.attempts == 5:
                        self.current_score = self.current_score + 4
                    if self.current_score > self.high_score:
                        self.high_score = self.current_score
                    Guessing_games.output(self)
                        
        except (TypeError, ValueError):
            print("Please provide valid input.")
        
    
    def level_hard(self):
        try:
            while self.attempts < 5 or self.guess != self.target_number:  
                self.guess = int(input("\n Enter your guess: "))
                if self.guess > self.target_number:
                    print(f"\n Wrong, guess lower")
                    self.attempts = self.attempts + 1
                    Guessing_games.helper(self)
                elif self.guess < self.target_number:
                    print(f"\n Wrong, guess higher")
                    self.attempts = self.attempts + 1
                    Guessing_games.helper(self)
                elif self.guess == self.target_number:
                    print(f"\n Correct! {self.target_number} was indeed the number!")
                    if self.attempts == 0:
                        self.current_score = self.current_score + 35
                    elif self.attempts == 1:
                        self.current_score = self.current_score + 30
                    elif self.attempts == 2:
                        self.current_score = self.current_score + 25
                    elif self.attempts == 3:
                        self.current_score = self.current_score + 20
                    elif self.attempts == 4:
                        self.current_score = self.current_score + 15
                    elif self.attempts == 5:
                        self.current_score = self.current_score + 10
                    if self.current_score > self.high_score:
                        self.high_score = self.current_score
                    Guessing_games.output(self)
                        
        except (TypeError, ValueError):
            print("Please provide valid input.")
                
    def output(self):
        
        print(f" \n Here is your scores : \n Score: {self.current_score} \n High score : {self.high_score}")
        replay = input("Would you like to play again? (y/n): ")
        if replay == 'y':
            Guessing_games.get_user_input(self)
            Guessing_games.difficulty_setter(self)
            Guessing_games.output(self)
        else:
            print("Thanks for playing!")
            quit()
print("-" * 40)
print(" - try and guess the correct number ! -")
print("-" * 40)
game = Guessing_games()
game.get_user_input()