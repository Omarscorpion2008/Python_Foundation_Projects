class csv_reader:
    def __init__(self):
        self.numerical_columns = []
        self.alphabet_columns = []
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
                print(f"Number of empty values in {key} : {self.number_of_empty_values}.")
            else:
                pass
        
        for key, values in self.database.items():
            if all(isinstance(v, (int, float)) for v in values):
                print(f"The column {key} is numeric")
                self.numerical_columns.append(self.database[key])

            elif all(isinstance(v, str) and v.isalpha() for v in values):
                print(f"The column {key} is alphabetic")
                self.alphabet_columns.append(self.database[key])

                
                
reader = csv_reader()