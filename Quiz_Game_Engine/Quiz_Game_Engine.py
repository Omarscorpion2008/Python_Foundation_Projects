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
        for question in self.questions:
            print(question)
            print(self.questions[question])
            user_input = input("Answer: ")
            self.user_answers.append(user_input)
    
    
Quiz()