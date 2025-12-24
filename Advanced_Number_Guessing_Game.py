from multiprocessing import Value
import random
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
        
    def input(self):
        self.difficulty = input("Choose the difficulty (e: easy | m: medium | h: hard | q: quit): ")
        
    def guessing_machine(self):
        self.attempts = 0
        self.current_score = 0
        try:    
            if self.difficulty != 'q':
            
                if self.difficulty == 'e':
                    self.target_number = random.randint(0, 20)
                elif self.difficulty == 'm':
                    self.target_number = random.randint(0, 100)
                elif self.difficulty == 'h':
                    self.target_number = random.randint(0, 300)
    
                while self.attempts <= 6 or self.guess != self.target_number:
                # EASY LEVEL
                    if self.difficulty.lower() == 'e':
                
                        self.guess = int(input("Enter your guess: "))

                        if self.guess > self.target_number:
                        
                            print(f"Wrong, guess lower")
                            self.attempts = self.attempts + 1
                        
                        elif self.guess < self.target_number:
                        
                            print(f"Wrong, guess higher")
                            self.attempts = self.attempts + 1
                        
                        elif self.guess == self.target_number:
                         
                            if self.attempts == 1:
                                self.current_score = self.current_score + 5
                            elif self.attempts == 2:
                                self.current_score = self.current_score + 4
                            elif self.attempts == 3:
                                self.current_score = self.current_score + 3
                            elif self.attempts == 2:
                                self.current_score = self.current_score + 2
                            elif self.attempts == 5:
                                self.current_score = self.current_score + 1
                        
                            if self.current_score > self.high_score:
                                self.high_score = self.current_score
                        
                            return self.current_score, self.high_score
                            
                    elif self.difficulty.lower() == 'm':
                    #MEDIUM LEVEL
                        self.guess = int(input("Enter your guess: "))

                        if self.guess > self.target_number:
                        
                            print(f"Wrong, guess lower")
                            self.attempts = self.attempts + 1
                        
                        elif self.guess < self.target_number:
                        
                            print(f"Wrong, guess higher")
                            self.attempts = self.attempts + 1
                        
                        elif self.guess == self.target_number:
                        
                            if self.attempts == 1:
                                self.current_score = self.current_score + 8
                            elif self.attempts == 2:
                                self.current_score = self.current_score + 7
                            elif self.attempts == 3:
                                self.current_score = self.current_score + 6
                            elif self.attempts == 2:
                                self.current_score = self.current_score + 5
                            elif self.attempts == 5:
                                self.current_score = self.current_score + 4
                        
                            if self.current_score > self.high_score:
                                self.high_score = self.current_score
                        
                            return self.current_score, self.high_score
                           
                    elif self.difficulty.lower() == 'h':
                    #HARD LEVEL
                        self.guess = int(input("Enter your guess: "))

                        if self.guess > self.target_number:
                        
                            print(f"Wrong, guess lower")
                            self.attempts = self.attempts + 1
                        
                        elif self.guess < self.target_number:
                        
                            print(f"Wrong, guess higher")
                            self.attempts = self.attempts + 1
                        
                        elif self.guess == self.target_number:
                        
                            if self.attempts == 1:
                                self.current_score = self.current_score + 30
                            elif self.attempts == 2:
                                self.current_score = self.current_score + 25
                            elif self.attempts == 3:
                                self.current_score = self.current_score + 20
                            elif self.attempts == 2:
                                self.current_score = self.current_score + 15
                            elif self.attempts == 5:
                                self.current_score = self.current_score + 10
                        
                            if self.current_score > self.high_score:
                                self.high_score = self.current_score

                            return self.current_score, self.high_score
                       
            elif self.difficulty == 'q':
                return "Thanks for using the game."
            
        except (TypeError, ValueError):
            return "Please use valid inputs: "    
    
    def output(self):
        
        print(f"Here is your scores : \n Score: {self.current_score} \n High score : {self.high_score}")
        replay = input("Would you like to play again? (y/n): ")
        if replay == 'y':
            self.input()
            self.guessing_machine()
            self.output()
        else:
            print("Thanks for playing!")
            exit

game = Guessing_games()

game.input()
game.guessing_machine()
game.output()