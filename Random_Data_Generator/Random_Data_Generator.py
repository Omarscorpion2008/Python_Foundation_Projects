import random
class Generator:
    def __init__(self):
        self.first_names = [
            "Alex", "Jordan", "Taylor", "Chris", "Sam",
            "Jamie", "Morgan", "Casey", "Riley", "Avery",
            "Dylan", "Cameron", "Parker", "Quinn", "Logan",
            "Ryan", "Emma", "Olivia", "Sophia", "Isabella",
            "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
            "Liam", "Noah", "Ethan", "Lucas", "Mason",
            "Aiden", "Elijah", "James", "Benjamin", "Henry"]
        
        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones",
            "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris",
            "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"]
        
        self.email_domains = [
            "gmail.com",
            "yahoo.com",
            "outlook.com",
            "hotmail.com"]
        
        self.names = []
        self.ages = []
        self.emails = []
        
        self.startup()
    
    def startup(self):
        self.number_of_generated_lines = int(input("How many lines would you like to generate? : "))
        self.fake_name_generator()
        self.fake_age_generator()
        self.fake_email_generator()
        self.data_saver()
    
    def fake_name_generator(self):
        for line in range(self.number_of_generated_lines):
            first_name = random.choice(self.first_names)
            last_name = random.choice(self.last_names)
            name = str(first_name + ' ' + last_name)
            self.names.append(name)
    
    def fake_age_generator(self):
        for line in range(self.number_of_generated_lines):
            age = random.randint(18,60)
            self.ages.append(age)
    
    def fake_email_generator(self):
        for line in range(self.number_of_generated_lines):
            name = self.names[line].replace(' ', '').lower()
            number = random.randint(0,3000)
            domain = random.choice(self.email_domains)
            email = str(name) + str(number) + '@' + str(domain)
            self.emails.append(email)
    
    def data_saver(self):
        pass
Generator()