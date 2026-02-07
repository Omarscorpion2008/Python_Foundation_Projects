class Scoreboard:
    def __init__(self):
        self.database = {}

        self.data_loader()
        self.menu()
        self.data_saver()
    
    def data_loader(self):
        try:
            with open(r'Game_ScoreBoard_System\database.csv','r', encoding='utf-8') as file:
                self.content = file.read()
                self.lines_list = self.content.splitlines()
                
                for line in self.lines_list:
                    items = line.split(',')
                    self.database[items[0]] = int(items[-1])
        except FileNotFoundError:
            pass

    def menu(self):
        while True:
            print('-' * 71)
            print(' ' * 26 + '- Game Scoreboard -')
            print('-' * 71)
            print(' Add Player (a) | Update Player Score (u) | View Scores (v) | exit (q)')
            user_input = input("What service do you prefer?: ").lower()
            if user_input == 'a':
                self.addition()
            elif user_input == 'u':
                self.update()
            elif user_input == 'v':
                self.view()
            elif user_input == 'q':
                print("Thanks for using the program.")
                break
            else:
                print("Please provide valid input.")

    def addition(self):
        while True: 
            user_name = input("Enter the player's name: ")
            user_score = int(input("Enter the player's starting score: "))
            if user_name in self.database:
                print("Player already exists, can't be added.")
            else:
                self.database[user_name] = user_score
                print("Player added successfully.")
                break

    def update(self):
        while True:
            user_name = input("Enter the player's name: ")
            user_score = int(input("Enter the player's gained score: "))
            if user_name in self.database:
                self.database[user_name] += user_score
                print("Player's score updated successfully")
                break
            else:
                print("Player's name not found in database")

    def view(self):
        database_sorted = sorted(self.database.items(), key=lambda item: item[1], reverse=True)
        print("Player | Score")
        for item in database_sorted:
            print(f'{item[0]} | {item[-1]}')

    def data_saver(self):
        with open(r'Game_ScoreBoard_System\database.csv','w',encoding='utf-8') as file:
            for key, value in self.database.items():
                file.write(f"{key},{value}\n")

Scoreboard()