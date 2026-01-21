from re import L


class csv_reader:
    def __init__(self):
        self.numerical_columns = []
        self.alphabet_columns = []
        self.unique_values = []
        self.occurrence_counter = {}
        self.database = {}
        self.data_loader()
    
    def data_loader(self):
        self.file = open('C:/Users/query1/Desktop/OmarScorpion2008/Python_Foundation_Projects/Manual_Csv_Reader/datafile.csv', 'r', encoding='utf-8')
        
        self.content = self.file.read()
        self.lines_list = self.content.splitlines()
        self.first_line = self.lines_list[0]
        self.first_line_items = self.first_line.split(',')
        self.data_lines = self.lines_list[1:]
        
        for item in self.first_line_items:
            self.database[str(item)] = []
            
        for row in self.data_lines:
            row_items = row.split(',')
            for item in row_items:
                
                if item.isalpha() :
                    self.database[list(self.database.keys())[row_items.index(item)]].append(str(item))
                elif item.isnumeric() :
                    self.database[list(self.database.keys())[row_items.index(item)]].append(float(item))
        self.data_analyzer()
        
    def data_analyzer(self):
            
        self.total_number_of_rows = len(self.data_lines)
        self.total_number_of_columns = len(self.database.keys())
        self.total_number_of_values = self.total_number_of_columns * self.total_number_of_rows
                    
        for key in self.database:
            self.number_of_empty_values = self.total_number_of_rows - len(self.database[key])
            if self.number_of_empty_values >= 1 :
                print(f"Number of empty values in {key} : {self.number_of_empty_values}")
            else:
                pass    
        if self.number_of_empty_values == 0:
            print("No Empty Values")
        
        for key, values in self.database.items():
            if all(isinstance(v, (int, float)) for v in values):
                print(f"The column {key} is numeric")
                self.numerical_columns.append(str(key))

            elif all(isinstance(v, str) and v.isalpha() for v in values):
                print(f"The column {key} is alphabetic")
                self.alphabet_columns.append(str(key))

        for key in self.numerical_columns:
            minimum_value = min(self.database[key])
            maximum_value = max(self.database[key])
            print(f"{key} column min/max values : {minimum_value} | {maximum_value}")
        
        for key in self.numerical_columns:
            total_number = sum(self.database[key])
            mean_number = total_number / len(self.database[key])
            print(f"{key} column sum/mean values : {total_number} | {mean_number}")
        
        for key in self.numerical_columns:
            middle_number = len(self.database[key]) / 2
            middle_value = sorted(self.database[key])[int(middle_number)]
            print(f"{key} median : {middle_value}")
        
        for key in self.numerical_columns:
            self.total_std_sum = 0
            mean_number = sum(self.database[key]) / len(self.database[key])
            
            for item in self.database[key]:
                self.total_std_sum = self.total_std_sum + (float(item) - float(mean_number))**2
                
            rational_equation = self.total_std_sum / (len(self.database[key]) - 1)
            sample_standard_deviation = rational_equation ** 0.5
            
            print(f"{key} std : {sample_standard_deviation:.2f}")
        
        for key in self.database:
            for item in self.database[key]:
                if item in self.unique_values:
                    pass
                else:
                    self.unique_values.append(item)
        number_of_unique_values = len(self.unique_values)
        print(f"Number of unique values : {number_of_unique_values}")
        
        for key in self.database:
            self.occurrence_counter[key] = []
            for item in self.database[key]:
                self.occurrence_counter[key].append(self.database[key].count(item))
        print(self.occurrence_counter)
reader = csv_reader()