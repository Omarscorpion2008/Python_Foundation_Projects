import time
class Timer:
    def user_input_classifier(self):
        self.user_input = input("Enter the time you want [HH:MM:SS]: ")
        self.parts = self.user_input.split(':')
        self.hours = float(self.parts[0])
        self.minutes = float(self.parts[1])
        self.seconds = float(self.parts[2])
    
    def Time_Calculator(self):
        pass