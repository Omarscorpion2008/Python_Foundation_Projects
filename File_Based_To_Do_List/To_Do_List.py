class to_do_list:
    def __init__(self):
        self.database = {}
        self.startup()

    def startup(self):
        user_input = input("Data Injection (i) | Load (l) | edit (e) | exit (q): ")
        if user_input.lower() == 'i':
            self.data_injection()
        elif user_input.lower() == 'l':
            self.data_loader()
        elif user_input.lower() == 'e':
            self.data_editor()
        elif user_input.lower() == 'q':
            print("Thanks for using the app!")
            exit()
        else:
            self.startup()

    def data_injection(self):

        self.file = open('File_Based_To_Do_List/list.txt', 'a', encoding='utf-8')
        user_input = 'test_value'

        while user_input != '':
            user_input = input("What would you like to add? : ")
            if user_input != '':
                self.file.write(f"{user_input},un-done\n")
            
        print("Data Injection completed.")
        self.file.close()

    def data_loader(self):
        self.file = open('File_Based_To_Do_List/list.txt', 'r', encoding='utf-8')
        self.content = self.file.read()
        self.lines_list = self.content.splitlines()

        for line in self.lines_list:
            items = line.split(',')
            self.database[items[0]] = str(items[-1])

        print("- un-done tasks -")
        for key, value in self.database.items():
            if value == 'un-done':
                print(f" {key}")

        self.file.close()

    def data_editor(self):
        self.file = open('File_Based_To_Do_List/list.txt', 'w', encoding='utf-8')

to_do = to_do_list()
