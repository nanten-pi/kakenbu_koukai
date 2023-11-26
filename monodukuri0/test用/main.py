import sensor
import math
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED1_pin=
LED2_pin=
GPIO.setup(LED1_pin, GPIO.OUT)
GPIO.setup(LED2_pin, GPIO.OUT)
while True:
    ax,ay,az=sensor.getAccel
    angle=math.degrees(math.atan(ax/az))
    print(angle)
    if angle<1:
        GPIO.output(LED1_pin,1)
        time.sleep(0.5)
        GPIO.output(LED1_pin,0)
    elif angle>1:
        GPIO.output(LED2_pin,1)
        time.sleep(0.5)
        GPIO.output(LED2_pin,0)
    else:
        GPIO.output(LED1_pin,0)
        GPIO.output(LED2_pin,0)
