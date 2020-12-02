from threading import Thread
from time import sleep
#import smbus2
#import bme280
from datetime import datetime, date
from camera import Cam
from microphone import audio
from tempHum import tempHumSensor

runtime = 10

'''class Sensor:
    def __init__(self):
        self._running = True
        self.port = 1
        self.address = 0x76
        self.bus = smbus2.SMBus(self.port)
        self.now = datetime.now()
        self.today = date.today()
        self.sensor_data = open("sensor_data","a")

    def terminate(self):
        self._running = False
        self.sensor_data.close()
                             
    def run(self):
        k=0
        while self._running:
            if k == 5:
                calibration_params = bme280.load_calibration_params(self.bus, self.address)
                data = bme280.sample(self.bus, self.address, calibration_params)
                k=0
                self.sensor_data.write(str(date.today())+"\t")
                self.sensor_data.write(str(datetime.now().strftime('%H:%M:%S'))+"\t")
                self.sensor_data.write(str(data.temperature)+"\t")
                self.sensor_data.write(str(data.humidity)+"\t\n") 
            sleep(1)
            k+=1'''
#microphone
audio = audio(runtime)
#run thread terminates after runtime
audioThread = Thread(target=audio.run)
audioThread.start()

Cam = Cam()
#Sensor = Sensor()
CamThread = Thread(target=Cam.run)
#SensorThread = Thread(target=Sensor.run)
CamThread.start()
#SensorThread.start()

#Temp Hum sensor
sensor = tempHumSensor()
sensorThread = Thread(target=sensor.run)
sensorThread.start()

sleep(runtime)
Cam.terminate()
sensor.terminate()
#Sensor.terminate()
print("Done")
                               
