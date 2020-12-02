import time
import datetime
import board
import adafruit_dht

class tempHumSensor:
    def __init__(self):
        self._running = True
        self.dhtDevice = adafruit_dht.DHT22(board.D4)
        self.pfad = '/home/pi/Documents/'
        self.name = self.pfad + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') + '.txt'
        self.my_file = open(self.name,"w+")

    def terminate(self):
        self._running = False
        self.my_file.close()
                             
    def run(self):
        k=0
        while self._running:
            if k == 2:
                k = 0

                try: 
                    temperature_c = self.dhtDevice.temperature
                    humidity = self.dhtDevice.humidity
                    self.my_file.write('Temperature: ' + str(temperature_c) + '°C, Humidity: ' + str(humidity) + '% \n')
        
                except RuntimeError as error:
                    #time.sleep(2.0)
                    print('Jetzt!')
                    continue
                
                except Exception as error:
                    self.dhtDevice.exit()
                    print('Hier!')
                    raise error
            
            time.sleep(1)
            k+=1
