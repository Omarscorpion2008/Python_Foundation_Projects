class Inventory:
    def __init__(self):
        self.data = {}
        self.data_load()
        self.startup()
        self.data_save()
    
    def startup(self):
        while True:
            print("-" * 90)
            print("Add product (a) | Update stock (u) | Sell stock (s) | show inventory value (v): ")
            print("-" * 90)
            user_input = input().lower()
            if user_input == 'a':
                self.product_addition()
            elif user_input == 'u':
                self.stock_update()
            elif user_input == 's':
                self.sell_stock()
            elif user_input == 'v':
                self.inventory_value()
            elif user_input == '':
                return
    
    def data_load(self):
        database = open('Inventory_Managment_System\\data.csv', 'r', encoding='utf-8')
        database_lines = database.readlines()
        
        for line in database_lines[1:]:
            items = line.split(',')
            self.data[items[0]] = list(map(float,items[1:]))

        print(self.data)

    def data_save(self):
        with open('Inventory_Managment_System\\data.csv','w', encoding='utf-8') as file:
            file.write('Product Name,Quantity,Price,Revenue\n')
            for key in self.data:
                line = str(key) + ',' + ','.join(map(str,self.data[key])) + '\n'
                file.write(line)

    def product_addition(self):

        while True:
            product_name = input("Enter the product's name: ").lower()
            if product_name != '':
                break
            else:
                print("Please enter a name.")
        
        while True:
            try:
                quantity_number = float(input("Enter the quantity number: "))

                if quantity_number <= 0:
                    print("Please enter a valid number")
                else:
                    break
            except ValueError:
                print("Enter a valid input.")
        
        while True:
            try:
                product_price = float(input("Enter the product price: "))
                if product_price <= 0 :
                    print("Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Enter a valid input.")

        if product_name in self.data.keys():
            print("Product already exists in database.")
        else:
            self.data[product_name] = [quantity_number,product_price,0]
            print("Product added successfully")
        
        print(self.data)

    def stock_update(self):
        while True:
            product = input("Which product stock are you modifying?: ")
            if product != '':
                break

        while True:
            restock_correction = input("Addition (a) | Subtraction (s): ").lower()
            if restock_correction == 'a':
                while True:
                    number = int(input("Enter the number to be added: "))
                    if number > 0:
                        self.data[product][0] += number
                        break
                    else:
                        print("please enter a valid number")
                        break
                break

            elif restock_correction == 's':
                while True:
                    number = int(input("Enter the number to be subtracted: "))
                    if number > 0:
                        check = self.data[product][0] - number
                        if check < 0:
                            print("can't make stock go into negative.")
                        else:
                            self.data[product][0] -= number
                        break
                    else:
                        print("Please enter a valid number")
                        break
                break
    
    def sell_stock(self):
        while True:
            product_name = input("Enter the product's name you are wishing to sell: ")
            if product_name != '':
                if product_name in self.data.keys():
                    break
        
        while True:
            number = int(input("How many pieces are you selling: "))
            if ( self.data[product_name][0] - number ) >= 0:
                self.data[product_name][0] -= number
                revenue = number * self.data[product_name][1]
                self.data[product_name][2] += revenue
                break
            else:
                print("Please enter a valid input.")
                break

        print(self.data)

    def inventory_value(self):
        total_inventory_value = 0
        total_revenue = 0

        for key in self.data.keys():
            buffer = self.data[key][0] * self.data[key][1]
            if buffer > 0:
                print(f"{key} total value: {buffer}")
                total_inventory_value = total_inventory_value + buffer
        
        for key in self.data.keys():
            total_revenue = total_revenue + self.data[key][2]

        print(f"Total inventory value: {total_inventory_value}")
        print(f"Total revenue value: {total_revenue}")
Inventory()