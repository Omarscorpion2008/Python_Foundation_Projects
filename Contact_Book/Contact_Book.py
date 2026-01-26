class Contact_Book:
    def __init__(self):
        self.contacts = []
        self.startup()

    def startup(self):
        self.data_loader()
        while True:
            user_input = input(
                "Would you like to Add (a) | Search (s) | Delete (d) | exit (q): "
            ).lower()

            if user_input == 'a':
                self.addition()
            elif user_input == 's':
                self.search()
            elif user_input == 'd':
                self.delete()
            elif user_input == 'q' or user_input == '':
                print("Goodbye.")
                break
            else:
                print("Invalid option.")

    def data_loader(self):
        self.contacts = []
        try:
            with open('Contact_Book/Contacts.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    name, number = line.strip().split(',')
                    self.contacts.append({name: number})
        except FileNotFoundError:
            pass

    def addition(self):
        user_name_input = input("Please provide the contact Name: ")
        user_number_input = input("Please provide the contact Number: ")
        user_name_exist = False

        for contact in self.contacts:
            if user_name_input in contact:
                user_name_exist = True
                break

        if user_name_exist:
            user_input = input("User already exists, would you like to still add it? (y/n): ").lower()
            if user_input != 'y':
                print("Contact hasn't been added.")
                return

        with open('Contact_Book/Contacts.txt', 'a', encoding='utf-8') as file:
            file.write(f"{user_name_input},{user_number_input}\n")

        self.contacts.append({user_name_input: user_number_input})
        print("Contact added successfully.")

    def search(self):
        user_answer = input("Which contact would you like to search for?: ").lower()

        found = False
        for contact in self.contacts:
            for name, number in contact.items():
                if user_answer in name.lower():
                    print(f"{name}: {number}")
                    found = True

        if not found:
            print("No matching contact found.")

    def delete(self):
        user_answer = input("Which contact would you like to delete?: ")

        new_contacts = []
        deleted = False

        for contact in self.contacts:
            if user_answer in contact:
                deleted = True
            else:
                new_contacts.append(contact)

        if not deleted:
            print("Contact not found.")
            return

        self.contacts = new_contacts

        with open('Contact_Book/Contacts.txt', 'w', encoding='utf-8') as file:
            for contact in self.contacts:
                for name, number in contact.items():
                    file.write(f"{name},{number}\n")

        print("Contact deleted successfully.")

Contact_Book()