#!/usr/bin/python
import sys, getopt
from time import sleep
import RPi.GPIO as GPIO
#from EmulatorGUI import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def gpio_steps(a,b,c,d,time):
    # Verwendete Pins(GPIP) am Rapberry Pi
    gpio_steps.time=0.0010
    gpio_steps.A=a
    gpio_steps.B=b
    gpio_steps.C=c
    gpio_steps.D=d
       
    # Pin aus Ausgabe definieren
    GPIO.setup(gpio_steps.A,GPIO.OUT)
    GPIO.setup(gpio_steps.B,GPIO.OUT)
    GPIO.setup(gpio_steps.C,GPIO.OUT)
    GPIO.setup(gpio_steps.D,GPIO.OUT)
    GPIO.output(gpio_steps.A, False)
    GPIO.output(gpio_steps.B, False)
    GPIO.output(gpio_steps.C, False)
    GPIO.output(gpio_steps.D, False)
    
    return (time)
    return (A, B, C, D)


# Schritte 1 - 8 definieren  
def Step1():
    GPIO.output(gpio_steps.D, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.D, False)


def Step2():
    GPIO.output(gpio_steps.D, True)
    GPIO.output(gpio_steps.C, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.D, False)
    GPIO.output(gpio_steps.C, False)


def Step3():
    GPIO.output(gpio_steps.C, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.C, False)


def Step4():
    GPIO.output(gpio_steps.B, True)
    GPIO.output(gpio_steps.C, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.B, False)
    GPIO.output(gpio_steps.C, False)


def Step5():
    GPIO.output(gpio_steps.B, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.B, False)


def Step6():
    GPIO.output(gpio_steps.A, True)
    GPIO.output(gpio_steps.B, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.A, False)
    GPIO.output(gpio_steps.B, False)


def Step7():
    GPIO.output(gpio_steps.A, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.A, False)


def Step8():
    GPIO.output(gpio_steps.D, True)
    GPIO.output(gpio_steps.A, True)
    sleep (gpio_steps.time)
    GPIO.output(gpio_steps.D, False)
    GPIO.output(gpio_steps.A, False)
 

###########################################
############### MAIN CLASS ############### 
###########################################
def main(argv):
   try:
      opts, args = getopt.getopt(argv,"ho:",["organ="])
   except getopt.GetoptError:
      print ('motor_head.py -o <organ>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('motor_head.py -o <organ>')
         sys.exit()
      elif opt in ("-o", "--organ"):
         organ = arg

   if organ == 'head':
      # Verwendete Pins(GPIP) am Rapberry Pi
      A=22
      B=23
      C=24
      D=25
      time = 0.0010
      
      gpio_steps(A,B,C,D,2) 
      print ('move head...')
         
      # Volle Umdrehung
      # da wir 4 magneten haben, brauchen wir 8 Schritte
      # 512 schritte sind eine 45 grad umdrehung;   512/8=64
      # 1024 schritte sind eine 90 grad umdrehung;   1024/8=128
      # 45vor      
      for i in range (64):  
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()  
          print (i)
      # 90zurueck
      for i in range (128):    
          Step8()  
          Step7()
          Step6()
          Step5()
          Step4()
          Step3()
          Step2()
          Step1()
          print (i)
      # 45vor
      for i in range (64):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print (i)
   elif organ == 'eyes':
      # Verwendete Pins(GPIP) am Rapberry Pi
      A=6
      B=12
      C=13
      D=5
      time = 0.0010
      
      gpio_steps(A,B,C,D,2) 
      print ('move eyes...')

      # Volle Umdrehung
      # da wir 4 magneten haben, brauchen wir 8 Schritte
      # 512 schritte sind eine 45 grad umdrehung;   512/8=64
      # 45vor
      for i in range (64):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print (i)
      # 90zurueck
      for i in range (128):
          Step8()
          Step7()
          Step6()
          Step5()
          Step4()
          Step3()
          Step2()
          Step1()
          print (i)
      # 45vor
      for i in range (64):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print (i)
          
      GPIO.cleanup()
    
   elif organ == 'jaw':
      # Verwendete Pins(GPIP) am Rapberry Pi
      A=20
      B=21
      C=19
      D=26
      time = 0.0010

      gpio_steps(A,B,C,D,2) 
      print ('move jaw...')

      # Volle Umdrehung
      # da wir 4 magneten haben, brauchen wir 8 Schritte
      # 512 schritte sind eine 45 grad umdrehung;   512/8=64
      # 90vor
      for i in range (128):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print (i)
      # 90zurueck
      for i in range (128):
          Step8()
          Step7()
          Step6()
          Step5()
          Step4()
          Step3()
          Step2()
          Step1()
          print (i)

      GPIO.cleanup()

if __name__ == "__main__":
   main(sys.argv[1:])

