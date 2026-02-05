class System:
    def __init__(self):
        self.action_score = 0
        self.comedy_score = 0
        self.drama_score = 0
        self.sci_fi_score = 0

        self.q1_answer = ''
        self.q2_answer = ''
        self.q3_answer = ''
        self.q4_answer = ''

        self.user_startup()
        self.rules()
        self.output()
    
    def user_startup(self):
        print('-' * 30)
        print(" - Recommendation System - ")
        print('-' * 30)
        print("\nPreferred Genre?")
        print("Action | Comedy | Drama | Sci-fi")
        self.q1_answer = input().lower().strip()
        while True:
            if self.q1_answer not in ['action', 'comedy', 'drama', 'sci-fi']:
                print("Please provide valid input.")
                self.q1_answer = input().lower().strip()
            else:
                break
        print("\nMood right now?")
        print("Relaxed | Excited | Serious")
        self.q2_answer = input().lower().strip()
        while True:
            if self.q2_answer not in ['relaxed', 'excited', 'serious']:
                print("Please provide valid input.")
                self.q2_answer = input().lower().strip()
            else:
                break
        print("\nHow much time do you have?")
        print("Short | Long")
        self.q3_answer = input().lower().strip()
        while True:
            if self.q3_answer not in ['short', 'long']:
                print("Please provide valid input.")
                self.q3_answer = input().lower().strip()
            else:
                break
        print("\nDo you like thinking-heavy movies?")
        print("Yes | No")
        self.q4_answer = input().lower().strip()
        while True:
            if self.q4_answer not in ['yes', 'no']:
                print("Please provide valid input.")
                self.q4_answer = input().lower().strip()
            else:
                break
        
    def rules(self):
        if self.q1_answer == 'action':
            self.action_score += 2
            self.sci_fi_score += 1
            self.drama_score += 1

        elif self.q1_answer == 'comedy':
            self.comedy_score += 2
            self.drama_score += 1
            self.action_score += 1

        elif self.q1_answer == 'drama':
            self.drama_score += 2
            self.action_score += 1
            self.comedy_score += 1

        else:
            self.sci_fi_score += 2
            self.action_score += 1
            self.drama_score += 1
        
        if self.q2_answer == 'relaxed':
            self.comedy_score += 2
            self.drama_score += 1
            self.action_score += 1

        elif self.q2_answer == 'excited':
            self.action_score += 2
            self.sci_fi_score += 2
            self.comedy_score += 1

        else:
            self.drama_score += 2
            self.sci_fi_score += 2
            self.action_score += 1

        if self.q3_answer == 'short':
            self.comedy_score += 2
            self.action_score += 2
            self.drama_score += 1
            self.sci_fi_score += 1

        else:
            self.drama_score += 2
            self.sci_fi_score += 2
            self.action_score += 1
            self.comedy_score += 1

        if self.q4_answer == 'yes':
            self.sci_fi_score += 2
            self.drama_score += 2
            self.action_score += 1
            self.comedy_score += 1
        else:
            self.comedy_score += 2
            self.action_score += 2
            self.drama_score += 1
            self.sci_fi_score += 1
    
    def output(self):
        print('-' * 20)
        print(' - Results - ')
        print('-' * 20)
    
        classes = ['action', 'comedy', 'drama', 'sci-fi']
        scores = [self.action_score, self.comedy_score, self.drama_score, self.sci_fi_score]
    
        max_score = max(scores)
        top_genres = [classes[i] for i, score in enumerate(scores) if score == max_score]

        if len(top_genres) == 1:
            print(f"You should go for {top_genres[0].capitalize()}")
        else:
            if self.q1_answer in top_genres:
                recommended = self.q1_answer
            else:
                recommended = top_genres[0]
            tie_genres = ', '.join([g.capitalize() for g in top_genres])
            print(f"There is a tie between: {tie_genres}")
            print(f"Recommended: {recommended.capitalize()} (matches your preference if possible)")
System()