import RPi.GPIO as GPIO
import time

# Set GPIO to Broadcom system and set RGB Pin numbers
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

color = red
GPIO.setup(color,GPIO.OUT)
print "LED on"
GPIO.output(color,GPIO.HIGH)
time.sleep(1)

print "LED off"
GPIO.output(color,GPIO.LOW)
