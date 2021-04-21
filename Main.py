import RPi.GPIO as GPIO
from Methoden import Pin
GPIO.setmode(GPIO.BCM) 

GPIO.setup(17, GPIO.OUT)
Pin.onoff("on",17)
