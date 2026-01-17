class Survey_Analyser:
    def __init__(self):

        self.total_satisfied = 0
        self.total_satisfied_list = []
        self.total_usability_score = 0
        self.total_usability_score_list = []
        self.total_recommendation = 0
        self.total_recommendation_list = []
        self.heard_from = []
        self.service_reusage = []
        self.service_expectation = []
        self.usage_frequency = []

        self.average_satisfaction = 0
        self.average_usability_score = 0
        self.average_recommendation_score = 0

        self.socialmedia_percentage = 0
        self.friend_percentage = 0
        self.advertisement_percentage = 0
        self.other_percentage = 0

        self.reusage_yes_percentage = 0
        self.reusage_no_percentage = 0

        self.expectations_yes_percentage = 0
        self.expectations_no_percentage = 0

        self.daily_percentage = 0
        self.weekly_percentage = 0
        self.monthly_percentage = 0
        self.rarely_percentage = 0
        self.startup()

    def startup(self):

        self.user_input = input("Data injection (i) or Data analyze (a) or quit (q): ")
        if self.user_input.lower() == 'i':
            self.questioner()
        elif self.user_input.lower() == 'a':
            self.parsing()
        elif self.user_input.lower() == 'q':
            print("Thanks for using our project! ")
            exit()
        else:
            print("Please provide valid input.")
            self.startup()
    
    def questioner(self):

        self.file = open('C:/Users/omara/OneDrive/Documents/GitHub/Python_Foundation_Projects/Survey_Analysis/database.txt', 'a', encoding='utf-8')

        q1 = input("How satisfied are you with our service? (1–5): ")
        while int(q1) not in list(range(1, 6)):
            print("Please provide a number in the range of 1-5.")
            q1 = input("How satisfied are you with our service? (1–5): ")
        self.file.write(f"{q1},")

        q2 = input("Rate the app usability from 1 (poor) to 10 (excellent): ")
        while int(q2) not in list(range(1, 11)):
            print("Please provide a number in the range of 1-10.")
            q2 = input("Rate the app usability from 1 (poor) to 10 (excellent): ")
        self.file.write(f"{q2},")

        q3 = input("How likely are you to recommend us? (0–10): ")
        while int(q3) not in list(range(0, 11)):
            print("Please provide a number in the range of 0-10.")
            q3 = input("How likely are you to recommend us? (0–10): ")
        self.file.write(f"{q3},")

        q4 = input("How did you hear about us? (Social Media, Friend, Advertisement, other): ")
        while q4 not in ['Social Media', 'Friend', 'Advertisement', 'other']:
            print("Please provide valid input, or check your spelling.")
            q4 = input("How did you hear about us? (Social Media, Friend, Advertisement, other): ")
        self.file.write(f"{q4},")

        q5 = input("Would you use this service again?(y/n): ").lower()
        while q5 not in ['y', 'n']:
            print("Please provide valid input.")
            q5 = input("Would you use this service again?(y/n): ").lower()
        self.file.write(f"{q5},")

        q6 = input("Did the program meet your expectations?(y/n): ").lower()
        while q6 not in ['y', 'n']:
            print("Please provide valid input.")
            q6 = input("Did the program meet your expectations?(y/n): ").lower()
        self.file.write(f"{q6},")

        q7 = input("How often do you use the app?(Daily, Weekly, Monthly, Rarely): ")
        while q7 not in ['Daily', 'Weekly', 'Monthly', 'Rarely']:
            print("Please provide valid input, or check your spelling.")
            q7 = input("How often do you use the app?(Daily, Weekly, Monthly, Rarely): ")
        self.file.write(f"{q7}\n")

        self.file.close()

        print("Data injection completed.")
        self.startup()

    def parsing(self):

        self.file = open('C:/Users/omara/OneDrive/Documents/GitHub/Python_Foundation_Projects/Survey_Analysis/database.txt', 'r', encoding='utf-8')
        
        content = self.file.read()
        lines_list = content.splitlines()
        for line in lines_list:
            buffer_list = line.split(',')
            
            self.total_satisfied = self.total_satisfied + int(buffer_list[0])
            self.total_satisfied_list.append(buffer_list[0])
            self.total_usability_score = self.total_usability_score + int(buffer_list[1])
            self.total_usability_score_list.append(buffer_list[1])
            self.total_recommendation = self.total_recommendation + int(buffer_list[2])
            self.total_recommendation.append(buffer_list[2])
            self.heard_from.append(buffer_list[3])
            self.service_reusage.append(buffer_list[4])
            self.service_expectation.append(buffer_list[5])
            self.usage_frequency.append(buffer_list[6])        

    def analyzer(self):

        self.average_satisfaction = self.total_satisfied / int(len(self.total_satisfied_list))
        self.average_usability_score = self.total_usability_score / int(len(self.total_usability_score_list))
        self.average_recommendation_score = self.total_recommendation / int(len(self.total_recommendation_list))

        self.socialmedia_percentage = (self.total_recommendation_list.count("Social Media") / len(self.total_recommendation_list)) * 100
        self.friend_percentage = (self.total_recommendation_list.count("Friend") / len(self.total_recommendation_list)) * 100
        self.advertisement_percentage = (self.total_recommendation_list.count("Advertisement") / len(self.total_recommendation_list)) * 100
        self.other_percentage = (self.total_recommendation_list.count("other") / len(self.total_recommendation_list)) * 100

        self.reusage_yes_percentage = (self.service_reusage.count("y") / len(self.service_reusage)) * 100
        self.reusage_no_percentage = (self.service_reusage.count("n") / len(self.service_reusage)) * 100

        self.expectations_yes_percentage = (self.service_expectation.count("y") / len(self.service_expectation)) * 100
        self.expectations_no_percentage = (self.service_expectation.count("n") / len(self.service_expectation)) * 100

        self.daily_percentage = (self.heard_from.count("Daily") / len(self.heard_from)) * 100
        self.weekly_percentage = (self.heard_from.count("Weekly") / len(self.heard_from)) * 100
        self.monthly_percentage = (self.heard_from.count("Monthly") / len(self.heard_from)) * 100
        self.rarely_percentage = (self.heard_from.count("Rarely") / len(self.heard_from)) * 100

        self.file.close()

        self.output()
    def output(self):
        pass

survey = Survey_Analyser()