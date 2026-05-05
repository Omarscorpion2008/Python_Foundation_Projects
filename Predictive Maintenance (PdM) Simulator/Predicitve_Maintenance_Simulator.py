import time
import random

class PdM:
    def __init__(self):
        
        self.safety = 0
        self.readings = {}
        
        for i in range(5):
            self.readings[i] = {'id' : i, 'temp' : random.uniform(49.7, 50.3), 'vib' : random.uniform(0.2, 0.8), 'temp_history' : [], 'vib_history' : [], 'state' : 'on'}

        while self.safety < ( 3/5 * len(self.readings.keys())):
            print("-" * 40)
            self.temp_simulation()
            self.check_health()
            self.prep()

    def temp_simulation(self):
        for i in range(5):
            for j in range(5):
                self.readings[j]['temp_history'].append(self.readings[j]['temp'])
                self.readings[j]['vib_history'].append(self.readings[j]['vib'])
                self.readings[j]['temp'] = random.uniform(self.readings[j]['temp'] - 1, self.readings[j]['temp'] + 3)
                self.readings[j]['vib'] = random.uniform(self.readings[j]['vib'] - 0.1, self.readings[j]['vib'] + 0.4)
        
    def check_health(self):
        file = open('Predictive Maintenance (PdM) Simulator\Report.csv', 'a', encoding='utf-8')

        for key in self.readings.keys():
            avg_temp = sum(self.readings[key]['temp_history']) / len(self.readings.keys())
            avg_vib = sum(self.readings[key]['vib_history']) / len(self.readings.keys())

            if avg_temp >= 80 and avg_vib >= 4.5:
                print(f"!!! CRITICAL SHUTDOWN: Machine {key} !!!")
                self.readings[key]['state'] = 'shutdown'
                file.write(f"{time.strftime("%H:%M:%S", time.localtime())},machine_{self.readings[key]['id']},{self.readings[key]['state']},{self.readings[key]['temp']}\n")

            elif avg_temp >= 70 or (2.8 < avg_vib < 4.5):
                print(f"Warning: Machine {key} requires inspection.")
                self.readings[key]['state'] = 'warning'
                file.write(f"{time.strftime("%H:%M:%S", time.localtime())},machine_{self.readings[key]['id']},{self.readings[key]['state']},{self.readings[key]['temp']}\n")


            elif self.readings[key]['temp_history'][-1] - self.readings[key]['temp_history'][0] > 5:
                print(f"Alert: Rapid temperature rise detected on Machine {key}")
        
        for key in self.readings.keys():
            if self.readings[key]['state'] == 'shutdown':
                self.safety += 1
        
        file.close()
    def prep(self):
        for key in self.readings.keys():
            self.readings[key]['temp_history'] = []
            self.readings[key]['vib_history'] = []
PdM() 