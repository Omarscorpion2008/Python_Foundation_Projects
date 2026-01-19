class csv_reader:
    def __init__(self):
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
        pass
reader = csv_reader()