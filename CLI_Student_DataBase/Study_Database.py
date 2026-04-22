class Student_Database:
    def __init__(self):
        self.data = {}
        self.data_load()
        self.startup()
        self.data_save()
    
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
                self.update_scores()
            elif user_input.lower() == 'g':
                self.gpa_calculation()
            elif user_input.lower() == 's':
                self.student_search()
            elif user_input.loweR() == '':
                exit()
    
    def data_load(self):
        database = open('CLI_Student_DataBase\\database.csv', 'r', encoding='utf-8')
        database_lines = database.readlines()
        
        for line in database_lines[1:]:
            items = line.split(',')
            self.data[int(items[0])] = items[1:]

        print(self.data)
    def data_save(self):
        pass

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
        student_id = int(input("Enter the student's id you which to update his score: "))
        student_subject = input("Enter the subject's abbreviation that you which to update: ")
        new_score = int(input("Enter the new score: "))

        if student_id in self.data.keys():
            while True:
                if student_subject.lower() == 'gl1':
                    self.data[student_id][1] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == 'eapss':
                    self.data[student_id][2] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == 'pfa1':
                    self.data[student_id][3] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == 'im':
                    self.data[student_id][4] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == 'calc1':
                    self.data[student_id][5] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == 'prog1':
                    self.data[student_id][6] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == 'ibi':
                    self.data[student_id][7] = new_score
                    print("Score updated successfully")
                    return
                elif student_subject == '':
                    return
        else:
            print("Student not found.")

    def gpa_calculation(self):
        student_id = int(input("Enter the student's id: "))
        total = 0
        if student_id in self.data.keys():
            credit_per_subj = [3, 3, 5, 5, 6, 6, 6]
            subjects = self.data[student_id][1:]

            for i in range(len(subjects)):
                subject_mark = credit_per_subj[i] * float(subjects[i])
                total = total + subject_mark
            
            gpa = total / sum(credit_per_subj)
            print(f"The student's gpa: {gpa:.2f}")
        else:
            print("Student not found")

    def student_search(self):
        student_id = int(input("Enter the student's id: "))
        if student_id in self.data.keys():
            print(f"Student's name: {self.data[student_id][0]}")
            print(f"German Langugae 1 score: {self.data[student_id][1]}")
            print(f"English for Academic Purposes and Study skills score: {self.data[student_id][2]}")
            print(f"Principles of Financial Accounting I score: {self.data[student_id][3]}")
            print(f"Introductions to Management score: {self.data[student_id][4]}")
            print(f"Math I (Calculus) score: {self.data[student_id][5]}")
            print(f"Programming I score: {self.data[student_id][6]}")
            print(f"Introduction to Business Informatics score: {self.data[student_id][7]}")
        else:
            print("Student not found.")

Student_Database()