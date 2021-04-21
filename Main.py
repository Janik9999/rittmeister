import RPi.GPIO as GPIO
from Methoden import Pin
GPIO.setmode(GPIO.BCM) 

Pin.onoff("on",17)
