import RPi.GPIO as GPIO
# GPIO setup

def rel(onoff, channel):
    if onoff== "on":
        GPIO.output(channel, GPIO.HIGH)
    elif onoff== "off":
        GPIO.output(channel, GPIO.LOW)
    else:
        print("Falsche Methoden Aufruf \n Benutze on off")
        