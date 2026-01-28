class Logs:
    def __init__(self):
        self.logs = {}
        self.error_count = 0
        self.warning_count = 0
        self.data_loader()
    
    def data_loader(self):
        self.file = open("Log_File_Analyzer/Logs.txt", 'r', encoding='utf-8')
        self.content = self.file.read()
        self.line_list = self.content.splitlines()
        log_list = []
        
        for line in self.line_list:
            line = line.strip()

            if 'ERROR' in line or 'error' in line:
                self.error_count += 1
            elif 'WARNING' in line or 'warning' in line:
                self.warning_count += 1
        
        for line in self.line_list:
            line = line.strip()

            parts = line.split()
            parts.pop(0)
            item = ' '.join(parts)

            if item:
                log_list.append(item)
        
        for item in log_list:
            self.logs[item] = log_list.count(item)
        
        self.output()
    
    def output(self):
        print("Log Summary")
        print('-' * 11)
        print(f"Errors: {self.error_count}")
        print(f"Warnings: {self.warning_count}")
        print("\nMost Frequent Messages:")

        sorted_d = dict(
            sorted(self.logs.items(), key=lambda item: item[1], reverse=True)
        )

        for i in range(2):
            print(f"{i}. {list(sorted_d)[i]} : {list(sorted_d.values())[i]}")
        
Logs()
