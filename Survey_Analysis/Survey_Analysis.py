class Survey_Analyser:
    def __init__(self):
        self.file = open('C:/Users/query1/Desktop/OmarScorpion2008/Python_Foundation_Projects/Survey_Analysis/database.txt', 'a+', encoding='utf-8')
        self.questioner()
        self.file.close()

    def questioner(self):
        q1 = input("How satisfied are you with our service? (1–5): ")
        self.file.write(f"{q1},")

        q2 = input("Rate the app usability from 1 (poor) to 10 (excellent): ")
        self.file.write(f"{q2},")

        q3 = input("How likely are you to recommend us? (0–10): ")
        self.file.write(f"{q3},")

        q4 = input("How did you hear about us? (Social Media, Friend, Advertisement, other): ")
        self.file.write(f"{q4},")

        q5 = input("Would you use this service again?(y/n): ")
        self.file.write(f"{q5},")

        q6 = input("Did the program meet your expectations?(y/n): ")
        self.file.write(f"{q6},")

        q7 = input("How often do you use the app?(Daily, Weekly, Monthly, Rarely): ")
        self.file.write(f"{q7},\n")
        self.analyser()

    def analyser(self):
        pass
survey = Survey_Analyser()