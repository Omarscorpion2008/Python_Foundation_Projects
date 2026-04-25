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
            self.data[items[0]] = items[1:]

        print(self.data)

    def data_save(self):
        with open('Inventory_Managment_System\\data.csv','w', encoding='utf-8') as file:
            file.write('Product Name,Quantity,Price\n')
            for key in self.data:
                line = str(key) + ',' + ','.join(map(str,self.data[key]))
                file.write(line)

    def product_addition(self):

        while True:
            product_name = input("Enter the product's name: ")
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
            self.data[product_name] = [quantity_number,product_price]
            print("Product added successfully")
        
        print(self.data)

    def stock_update(self):
        pass

    def sell_stock(self):
        pass

    def inventory_value(self):
        pass

Inventory()