class Inventory:
    def __init__(self):
        self.data = {}
        self.data_load()
        self.startup()
    
    def startup(self):
        while True:
            user_input = input("Add product (a) | Update stock (u) | Sell stock (s) | show inventory value (v): ")
            if user_input.lower() == 'a':
                self.product_addition()
            elif user_input.lower() == 'u':
                self.stock_update()
            elif user_input.lower() == 's':
                self.sell_stock()
            elif user_input.lower() == 'v':
                self.inventory_value()
            elif user_input.lower() == '':
                return
    
    def data_load(self):
        pass
            