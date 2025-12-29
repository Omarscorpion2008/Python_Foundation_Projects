import time
class Timer:
    def user_input_classifier(self):
        self.user_input = input("Enter the time you want [HH:MM:SS]: ")
        self.parts = self.user_input.split(':')
        self.hours = float(self.parts[0])
        self.minutes = float(self.parts[1])
        self.seconds = float(self.parts[2])
        
        Timer.Time_Calculator(self)
    def Time_Calculator(self):
        self.hours = self.hours * 3600
        self.minutes = self.minutes * 60
        
        self.total_time = self.hours + self.minutes + self.seconds
        Timer.Time_Passing_mechanism(self)
    def Time_Passing_mechanism(self):
        while self.total_time > 0 :
            print(time)
            time.sleep(1)
            self.total_time = self.total_time - 1

countdown = Timer()
countdown.user_input_classifier()