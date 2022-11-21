#shutdown GPIO which is longer aktiv as allowed

from datetime import datetime
import time
from Methoden import Wert
from Methoden import Pin
import RPi.GPIO as GPIO

#to avoid that its running befor relais-logge.py
time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

L1 = open("rittmeister/time_stamp.txt", "r") 
L1=list(map(str,L1.read().split("#")))
max_open_interval = datetime.strptime("00:00:01", "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S")

x=0   
y=0  

while x < len(L1):
    if L1[x] != "0":
        print(L1[x])
        y = datetime.strptime(datetime.today().strftime("%d.%m.%Y.%H:%M:%S"), "%d.%m.%Y.%H:%M:%S") - datetime.strptime(L1[x], "%d.%m.%Y.%H:%M:%S")
        if y > max_open_interval:
            Wert.dek()
            GPIO.setup(x + 1, GPIO.OUT)
            Pin.rel("off",x + 1)
    x = x + 1
