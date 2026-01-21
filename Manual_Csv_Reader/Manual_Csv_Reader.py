class csv_reader:
    def __init__(self):
        self.numerical_columns = []
        self.alphabet_columns = []
        self.unique_values = []
        self.database = {}
        self.data_loader()
    
    def data_loader(self):
        self.file = open('C:/Users/omara/OneDrive/Documents/GitHub/Python_Foundation_Projects/Manual_Csv_Reader/datafile.csv', 'r', encoding='utf-8')
        
        self.content = self.file.read()
        self.lines_list = self.content.splitlines()
        self.first_line = self.lines_list[0]
        self.first_line_items = self.first_line.split(',')
        self.data_lines = self.lines_list[1:]
        
        for item in self.first_line_items:
            self.database[str(item)] = []
            
        for row in self.data_lines:
            row_items = row.split(',')
            for index, value in enumerate(row_items):
                try:
                    self.database[list(self.database.keys())[index]].append(float(value))
                except ValueError:
                    self.database[list(self.database.keys())[index]].append(value)
        self.data_analyzer()
        self.file.close()

    def data_analyzer(self):
            
        self.total_number_of_rows = len(self.data_lines)
        self.total_number_of_columns = len(self.database.keys())
        self.total_number_of_values = self.total_number_of_columns * self.total_number_of_rows

        print('-' * 50)

        for key in self.database:
            self.number_of_empty_values = self.total_number_of_rows - len(self.database[key])
            if self.number_of_empty_values >= 1 :
                print(f"Number of empty values in {key} : {self.number_of_empty_values}")
            else:
                print(f"No Empty Values in {key} column")

        print('-' * 50)

        for key, values in self.database.items():
            if all(isinstance(v, (int, float)) for v in values):
                print(f"The column {key} is numeric")
                self.numerical_columns.append(str(key))

            elif all(isinstance(v, str) for v in values):
                print(f"The column {key} is alphabetic")
                self.alphabet_columns.append(str(key))

        print('-' * 50)

        for key in self.numerical_columns:
            minimum_value = min(self.database[key])
            maximum_value = max(self.database[key])
            print(f"{key} column min/max values : {minimum_value} | {maximum_value}")
        
        print('-' * 50)

        for key in self.numerical_columns:
            total_number = sum(self.database[key])
            mean_number = total_number / len(self.database[key])
            print(f"{key} column sum/mean values : {total_number} | {mean_number}")
        
        print('-' * 50)

        for key in self.numerical_columns:
            sorted_list = sorted(self.database[key])
            n = len(sorted_list)
            if n % 2 == 1:
                median = sorted_list[n//2]
            else:
                median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
                
            print(f"{key} median : {median}")
        
        print('-' * 50)

        for key in self.numerical_columns:
            self.total_std_sum = 0
            mean_number = sum(self.database[key]) / len(self.database[key])
            
            for item in self.database[key]:
                self.total_std_sum = self.total_std_sum + (float(item) - float(mean_number))**2
                
            rational_equation = self.total_std_sum / (len(self.database[key]))
            population_standard_deviation = rational_equation ** 0.5
            
            print(f"{key} std : {population_standard_deviation:.2f}")
        
        print('-' * 50)

        for key in self.database:
            self.unique_values = []
            for item in self.database[key]:
                if item in self.unique_values:
                    pass
                else:
                    self.unique_values.append(item)
            number_of_unique_values = len(self.unique_values)
            print(f"Number of unique values in {key} column : {number_of_unique_values}")
        
        print('-' * 50)

        for key in self.database:
            counts = {}

            for item in self.database[key]:
                if item in counts:
                    counts[item] += 1
                else:
                    counts[item] = 1

            max_count = max(counts.values())
            mode = [item for item, count in counts.items() if count == max_count]

            print(f"\n{key} mode:\n{mode}\ncount:{max_count}",end='\n')
        
        print('-' * 50)

        for key in self.database:
            percentage = 0
            print(f"{key} :",end='')
            for item in set(self.database[key]):
                percentage = ( self.database[key].count(item) / len(self.database[key])) * 100
                print(f"\n{item} : {percentage:.2f}%", end='')
            print('\n' + '-' * 50)

reader = csv_reader()