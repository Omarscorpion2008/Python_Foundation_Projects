class Quiz:
    def __init__(self):
        self.questions = {}
        self.answers = {}
        self.user_answers = []
        self.score = 0
        self.data_loader()
        
    def data_loader(self):
        self.file = open("Quiz_Game_Engine/Quiz_Questions.txt", 'r', encoding='utf-8')
        self.content = self.file.read()
        self.lines_list = self.content.splitlines()
        
        for line in self.lines_list:
            items = line.split(',')
            self.questions[items[0]] = items[1:-1]
            self.answers[items[0]] = items[-1]
        
        self.Ask()
        
    def Ask(self):
        letters = ['A', 'B', 'C', 'D']
        for question in self.questions:
            print("\n" + question)
            for i, choice in enumerate(self.questions[question]):
                print(f"{letters[i]}) {choice}")
            user_input = input("Answer: ").upper()
            self.user_answers.append(user_input)
    
        self.score_checker()

    
    def score_checker(self):
        for answer in range(len(self.user_answers)):
            if list(self.answers.values())[answer] == self.user_answers[answer]:
                print(f"Question Number {answer} was answered correctly !")
                self.score = self.score + 1
            else:
                print(f"Question Number {answer} was answered wrongly :(")
        self.output()
    
    def output(self):
        self.total_question_count = len(list(self.questions))
        score_percentage = ( self.score / len(list(self.questions)) ) * 100
        
        print("Quiz Complete!")
        print(f"You scored {self.score} out of {self.total_question_count} ({score_percentage:.2f}%)")
        
        if score_percentage < 50:
            print("\nYou certainly can do better bro")
        else:
            print("\nNice job!")
Quiz()