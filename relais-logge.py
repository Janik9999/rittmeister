# checks if GPIO is on and give it a timestamp

from datetime import datetime
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

L1 = []
L2 = open("rittmeister/time_stamp.txt", "r")
L2=list(map(str,L2.read().split("#")))

x=0

for x in range(1, 26):
    GPIO.setup(x, GPIO.OUT)
    L1.append(GPIO.input(x))

x=0     

while x < len(L1):

    if L1[x] == 1:
        if L2[x] == "0":
            L2[x] = datetime.today().strftime("%d.%m.%Y.%H:%M:%S")
    else:
        L2[x] = "0"
    x = x + 1

print(L2)

with open('rittmeister/time_stamp.txt', 'w') as time:
    tren="#"
    time.write(tren.join(L2))
