class Calculator:
    def user_input_classifier(self):
        self.celsius = 0.0
        self.fahrenheit = 0.0
        self.kelvin = 0.0
        self.buffer = ''
        self.user_input = input("Enter an Expression: ")
        
        if self.user_input == '':
            print("Thanks for using our conversion app.")
            exit()
        
        for character in self.user_input:
            
            if character.isnumeric() or character == '.' or character == '-':
                self.buffer = self.buffer + character
            elif character == ' ':
                continue
            elif character.isalpha():
                if character.upper() == 'C':
                    self.celsius = float(self.buffer)
                elif character.upper() == 'F':
                    self.fahrenheit = float(self.buffer)
                elif character.upper() == 'K':
                    self.kelvin = float(self.buffer)
        
        if self.celsius == 0 or self.fahrenheit == 0 or self.kelvin == 0:
            print("Please provide a valid input.")
            self.user_input_classifier()
            
        self.transformation_chooser()
    def transformation_chooser(self):
        self.transfer_to = input("What unit do you want to transfer this to ?(C: Celsius | F: Fahrenheit | K: Kelvin): ")
        
        if self.fahrenheit == 0 and self.kelvin == 0 and self.transfer_to.upper() == 'F':
            self.Celsius_to_Fahrenheit()
        elif self.fahrenheit == 0 and self.kelvin == 0 and self.transfer_to.upper() == 'K':
            self.Celsius_to_Kelvin()
        elif self.fahrenheit == 0 and self.kelvin == 0 and self.transfer_to.upper() == 'C':
            print(f"{self.celsius} °C")
        elif self.celsius == 0 and self.kelvin == 0 and self.transfer_to.upper() == 'F':
            print(f"{self.fahrenheit} °F")
        elif self.celsius == 0 and self.kelvin == 0 and self.transfer_to.upper() == 'K':
            self.Fahrenheit_to_Kelvin()
        elif self.celsius == 0 and self.kelvin == 0 and self.transfer_to.upper() == 'C':
            self.Fahrenheit_to_Celsius()
        elif self.fahrenheit == 0 and self.celsius == 0 and self.transfer_to.upper() == 'F':
            self.Kelvin_to_Fahrenheit()
        elif self.fahrenheit == 0 and self.celsius == 0 and self.transfer_to.upper() == 'K':
            print(f"{self.kelvin}")
        elif self.fahrenheit == 0 and self.celsius == 0 and self.transfer_to.upper() == 'C':
            self.Kelvin_to_Celsius()
        
    def Celsius_to_Fahrenheit(self):
        self.result = (self.celsius * 1.8) + 32
        print(f"Result: {self.result:.2f} °F")
    def Celsius_to_Kelvin(self):
        self.result = self.celsius + 273.15
        print(f"Result: {self.result:.2f}")
    def Fahrenheit_to_Celsius(self):
        self.result = (self.fahrenheit - 32) / 1.8
        print(f"Result: {self.result:.2f} °C")
    def Fahrenheit_to_Kelvin(self):
        self.result = ((self.fahrenheit - 32) / 1.8) + 273.15
        print(f"Result: {self.result:.2f}")
    def Kelvin_to_Celsius(self):
        self.result = self.kelvin - 273.15
        print(f"Result: {self.result:.2f} °C")
    def Kelvin_to_Fahrenheit(self):
        self.result = ((self.kelvin - 273.15) * 1.8) + 32
        print(f"Result: {self.result:.2f} °F")
        
calc = Calculator()

print('-' * 21)
print(' - Unit Conversion -')
print('-' * 21)
while True:
    try:
        calc.user_input_classifier()
    except (TypeError, ValueError):
        print("Please provide valid input.")
        calc.user_input_classifier()
