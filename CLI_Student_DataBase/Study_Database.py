class Student_Database:
    def __init__(self):
        self.data = {}
        self.data_load()
        self.startup()
    
    def startup(self):
        while True:
            print('-' * 100)
            print("  add student (a) | delete student (d) | update grades (u) | calculate gpa (g) | search by ID (s): ")
            print('-' * 100)
            user_input = input("")

            if user_input.lower() == 'a':
                self.student_addtion()
            elif user_input.lower() == 'd':
                self.student_subtraction()
            elif user_input.lower() == 'u':
                pass
            elif user_input.lower() == 'g':
                pass
            elif user_input.lower() == 's':
                pass
    
    def data_load(self):
        database = open('CLI_Student_DataBase\\database.csv', 'r', encoding='utf-8')
        database_lines = database.readlines()
        
        for line in database_lines[1:]:
            items = line.split(',')
            self.data[int(items[0])] = items[1:]

    def student_addtion(self):
        print("Enter the student's details: ")
        name = str(input("Student Name: "))
        GL1 = int(input("German Language 1 grades: "))
        EAPSS = int(input("English for Academic Purposes and Study Skills grades: "))
        PFA1 = int(input("Principles of Financial Accounting 1 grades: "))
        IM = int(input("Introduction to Managment grades: "))
        CALC1 = int(input("Calculus 1 grades: "))
        PROG1 = int(input("Programming 1 grades: "))
        IBI = int(input("Introduction to Business Informatics grades: "))
        id = int(list(self.data.keys())[-1]) + int(1)
        self.data[id] = [name, GL1, EAPSS, PFA1, IM, CALC1, PROG1, IBI]
        print("Student added successfully")

    def student_subtraction(self):
        user_input = int(input("Enter the student's id: "))
        if user_input in self.data:
            del self.data[user_input]
            print("Student deleted successfully.")
        else:
            print("Student not found in database.")

    def update_scores(self):
        pass

    def gpa_calculation(self):
        pass
    
    def student_search(self):
        pass

Student_Database()