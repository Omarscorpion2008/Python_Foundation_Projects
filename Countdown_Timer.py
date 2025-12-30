import time
class Timer:
    def user_input_classifier(self):
        self.user_input = input("Enter the time you want [HH:MM:SS]: ")
        self.parts = self.user_input.split(':')
        self.hours = int(self.parts[0])
        self.minutes = int(self.parts[1])
        self.seconds = int(self.parts[2])
        
        if self.user_input != '':
            Timer.Time_Calculator(self)
        else:
            print("Thanks for using the Countdown.")
            exit()
            

    def Time_Calculator(self):
        self.hours = self.hours * 3600
        self.minutes = self.minutes * 60
        self.total_time = self.hours + self.minutes + self.seconds
        Timer.Time_Passing_mechanism(self)

    def Time_Passing_mechanism(self):
        for current_countdown in range(self.total_time, 0, -1):
            self.hours = int((current_countdown / 60) / 60) % 60
            self.minutes = int(current_countdown / 60) % 60
            self.seconds = int(current_countdown % 60)
            print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")
            time.sleep(1)
        print("! TIME'S UP !")

countdown = Timer()
while True:
    try:
        countdown.user_input_classifier()
    except (ValueError, TypeError, IndexError):
        print("Please provide valid inputs.")
        countdown.user_input_classifier()