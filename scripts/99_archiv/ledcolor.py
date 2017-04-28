#!/usr/bin/python

import sys, getopt
import RPi.GPIO as GPIO
import time

# Set GPIO to Broadcom system and set RGB Pin numbers
RUNNING = True
GPIO.setmode(GPIO.BCM)
gpio_red = 17
gpio_green = 18
gpio_blue = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def main(argv):
   color = ''
   duration = '2'
   try:
      opts, args = getopt.getopt(argv,"hc:d:",["color=","duration="])
   except getopt.GetoptError:
      print 'test.py -c <color> -d <duration>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -c <color> -d <duration>'
         sys.exit()
      elif opt in ("-c", "--color"):
         color = arg
      elif opt in ("-d", "--duration"):
         duration = arg

   # color stuff
   if color == 'red':
      gpio_color = gpio_red
   elif color == 'green':
      gpio_color = gpio_green
   elif color == 'blue':
      gpio_color = gpio_blue

   # output
   print 'LED color is: ', color, '[', gpio_color, ']'
   print 'LED duration is: ', duration
   print ""

   GPIO.setup(gpio_color,GPIO.OUT)
   print "LED", color, "on"
   GPIO.output(gpio_color,GPIO.HIGH)
   time.sleep(float(duration))
   
   print "LED", color, "off"
   GPIO.output(gpio_color,GPIO.LOW)

if __name__ == "__main__":
   main(sys.argv[1:])
