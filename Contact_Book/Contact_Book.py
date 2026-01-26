class Contact_Book:
    def __init__(self):
        self.contacts = []
        self.startup()
    
    def startup(self):
        while True:
            self.data_loader()
            try:
                user_input = input("Would you like to Add (a) | Search (s) | Delete (d) | exit (q) a contact: ")
                if user_input.lower() == 'a':
                    self.addition()
                elif user_input.lower() == 's':
                    self.search()
                elif user_input.lower() == 'd':
                    self.delete()
                elif user_input.lower() == 'q' or user_input.lower() == '':
                    exit()
            except ValueError:
                print("Please provide valid input.")
                self.startups()
    
    def data_loader(self):
        pass

    def addition(self):
        pass

    def search(self):
        pass
    
    def delete(self):
        pass