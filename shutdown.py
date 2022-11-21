import RPi.GPIO as GPIO
import time
from Methoden import Wert 
from Methoden import Pin
import paho.mqtt.publish as publish
from Methoden import mqtt_rec
import threading
import sys

Wert.dek()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(1, GPIO.OUT)
Pin.rel("off",int(sys.argv[1])) 
