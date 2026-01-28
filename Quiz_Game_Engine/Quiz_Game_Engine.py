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
    
        for index, question in enumerate(self.questions):
            print("\n" + question)
            for i, choice in enumerate(self.questions[question]):
                print(f"{letters[i]}) {choice}")
        
            user_input = input("Answer: ").upper()
            self.user_answers.append(user_input)

            correct_answer = list(self.answers.values())[index]
            if user_input == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}\n")
    
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