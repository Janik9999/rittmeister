import RPi.GPIO as GPIO
import time
from Methoden import Wert 
from Methoden import Pin
import paho.mqtt.publish as publish
from Methoden import mqtt_rec
import threading

Wert.dek()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(1, GPIO.OUT)
Pin.rel("off",1) 
GPIO.setup(2, GPIO.OUT)
Pin.rel("off",2) 
GPIO.setup(3, GPIO.OUT)
Pin.rel("off",3) 
GPIO.setup(4, GPIO.OUT)
Pin.rel("off",4) 
GPIO.setup(5, GPIO.OUT)
Pin.rel("off",5) 
GPIO.setup(6, GPIO.OUT)
Pin.rel("off",6) 
GPIO.setup(7, GPIO.OUT)
Pin.rel("off",7) 
GPIO.setup(8, GPIO.OUT)
Pin.rel("off",8)

GPIO.setup(27, GPIO.OUT)
Pin.rel("off",27) 
class myFred(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD=iD
        self.name=name
    
    def run(self):
        mqtt_rec.client = mqtt_rec.mqtt.Client()
        mqtt_rec.client.on_connect = mqtt_rec.on_connect
        mqtt_rec.client.on_message = mqtt_rec.on_message
        mqtt_rec.client.connect("localhost", 1883, 60)
        mqtt_rec.client.loop_forever()
        
        
class myFred2(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD=iD
        self.name=name
    
    def run(self):
        Pin.rel("on",27)
        time.sleep(15)
        Pin.rel("off",27) 
        
t1=myFred(1,"t1")
t1.start()
while (True):
    time.sleep(1)
    print(Wert.Fach)
    if(len(Wert.Fach)!=0):
        t2=myFred2(2,"t2")
        t2.start()
        while(len(Wert.Fach)!=0):
            Pin.rel("on",int(Wert.Fach[0]))
            time.sleep(3)
            Pin.rel("off",int(Wert.Fach[0]))   
            Wert.Fach.remove(Wert.Fach[0])

        
 