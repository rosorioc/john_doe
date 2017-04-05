#!/usr/bin/python

import sys, getopt
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

## Pins aus Ausgae definieren
#GPIO.setup(A,GPIO.OUT)
#GPIO.setup(B,GPIO.OUT)
#GPIO.setup(C,GPIO.OUT)
#GPIO.setup(D,GPIO.OUT)
#GPIO.output(A, False)
#GPIO.output(B, False)
#GPIO.output(C, False)
#GPIO.output(D, False)
#
## Schritte 1 - 8 definieren
#def Step1():
#    GPIO.output(D, True)
#    sleep (time)
#    GPIO.output(D, False)
#
#def Step2():
#    GPIO.output(D, True)
#    GPIO.output(C, True)
#    sleep (time)
#    GPIO.output(D, False)
#    GPIO.output(C, False)
#
#def Step3():
#    GPIO.output(C, True)
#    sleep (time)
#    GPIO.output(C, False)
#
#def Step4():
#    GPIO.output(B, True)
#    GPIO.output(C, True)
#    sleep (time)
#    GPIO.output(B, False)
#    GPIO.output(C, False)
#
#def Step5():
#    GPIO.output(B, True)
#    sleep (time)
#    GPIO.output(B, False)
#
#def Step6():
#    GPIO.output(A, True)
#    GPIO.output(B, True)
#    sleep (time)
#    GPIO.output(A, False)
#    GPIO.output(B, False)
#
#def Step7():
#    GPIO.output(A, True)
#    sleep (time)
#    GPIO.output(A, False)
#
#def Step8():
#    GPIO.output(D, True)
#    GPIO.output(A, True)
#    sleep (time)
#    GPIO.output(D, False)
#    GPIO.output(A, False)

def main(argv):
   organ = ''
   try:
      opts, args = getopt.getopt(argv,"ho:",["organ="])
   except getopt.GetoptError:
      print 'motor_head.py -o <organ>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'motor_head.py -o <organ>'
         sys.exit()
      elif opt in ("-o", "--organ"):
         organ = arg

   if organ == 'head':
      # Verwendete Pins(GPIP) am Rapberry Pi
      A=22
      B=23
      C=24
      D=25
      #time = 0.005
      time = 0.0010

    # Pins aus Ausgae definieren
      GPIO.setup(A,GPIO.OUT)
      GPIO.setup(B,GPIO.OUT)
      GPIO.setup(C,GPIO.OUT)
      GPIO.setup(D,GPIO.OUT)
      GPIO.output(A, False)
      GPIO.output(B, False)
      GPIO.output(C, False)
      GPIO.output(D, False)

      # Schritte 1 - 8 definieren
      def Step1():
          GPIO.output(D, True)
          sleep (time)
          GPIO.output(D, False)

      def Step2():
          GPIO.output(D, True)
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(D, False)
          GPIO.output(C, False)

      def Step3():
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(C, False)

      def Step4():
          GPIO.output(B, True)
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(B, False)
          GPIO.output(C, False)

      def Step5():
          GPIO.output(B, True)
          sleep (time)
          GPIO.output(B, False)

      def Step6():
          GPIO.output(A, True)
          GPIO.output(B, True)
          sleep (time)
          GPIO.output(A, False)
          GPIO.output(B, False)

      def Step7():
          GPIO.output(A, True)
          sleep (time)
          GPIO.output(A, False)

      def Step8():
          GPIO.output(D, True)
          GPIO.output(A, True)
          sleep (time)
          GPIO.output(D, False)
          GPIO.output(A, False)

      # Volle Umdrehung
      # da wir 4 magneten haben, brauchen wir 8 Schritte
      # 512 schritte sind eine 45 grad umdrehung;   512/8=64
      # 1024 schritte sind eine 90 grad umdrehung;   1024/8=128
      #45vor      
      for i in range (64):    
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()  
          print i
      #90zurueck
      for i in range (128):    
          Step8()  
          Step7()
          Step6()
          Step5()
          Step4()
          Step3()
          Step2()
          Step1()
          print i
      #45vor
      for i in range (64):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print i
   elif organ == 'eyes':
      # Verwendete Pins(GPIP) am Rapberry Pi
      A=6
      B=12
      C=13
      D=5
      #time = 0.005
      time = 0.0010

      # Pins aus Ausgae definieren
      GPIO.setup(A,GPIO.OUT)
      GPIO.setup(B,GPIO.OUT)
      GPIO.setup(C,GPIO.OUT)
      GPIO.setup(D,GPIO.OUT)
      GPIO.output(A, False) 
      GPIO.output(B, False)
      GPIO.output(C, False)
      GPIO.output(D, False) 
      
      # Schritte 1 - 8 definieren
      def Step1():
          GPIO.output(D, True)
          sleep (time)
          GPIO.output(D, False)
      
      def Step2(): 
          GPIO.output(D, True)
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(D, False)
          GPIO.output(C, False)
      
      def Step3():
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(C, False)
      
      def Step4(): 
          GPIO.output(B, True)
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(B, False)
          GPIO.output(C, False)
      
      def Step5():
          GPIO.output(B, True)
          sleep (time)
          GPIO.output(B, False)
      
      def Step6(): 
          GPIO.output(A, True)
          GPIO.output(B, True)
          sleep (time)
          GPIO.output(A, False)
          GPIO.output(B, False)
      
      def Step7():
          GPIO.output(A, True)
          sleep (time)
          GPIO.output(A, False)
      
      def Step8():
          GPIO.output(D, True)
          GPIO.output(A, True)
          sleep (time)
          GPIO.output(D, False)
          GPIO.output(A, False)

      # Volle Umdrehung
      # da wir 4 magneten haben, brauchen wir 8 Schritte
      # 512 schritte sind eine 45 grad umdrehung;   512/8=64
      #45vor

      for i in range (64):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print i
      #90zurueck
      for i in range (128):
          Step8()
          Step7()
          Step6()
          Step5()
          Step4()
          Step3()
          Step2()
          Step1()
          print i
      #45vor
      for i in range (64):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print i
   elif organ == 'jaw':
      # Verwendete Pins(GPIP) am Rapberry Pi
      A=20
      B=21
      C=19
      D=26
      #time = 0.005
      time = 0.0010

    # Pins aus Ausgae definieren
      GPIO.setup(A,GPIO.OUT)
      GPIO.setup(B,GPIO.OUT)
      GPIO.setup(C,GPIO.OUT)
      GPIO.setup(D,GPIO.OUT)
      GPIO.output(A, False)
      GPIO.output(B, False)
      GPIO.output(C, False)
      GPIO.output(D, False)

      # Schritte 1 - 8 definieren
      def Step1():
          GPIO.output(D, True)
          sleep (time)
          GPIO.output(D, False)

      def Step2():
          GPIO.output(D, True)
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(D, False)
          GPIO.output(C, False)

      def Step3():
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(C, False)

      def Step4():
          GPIO.output(B, True)
          GPIO.output(C, True)
          sleep (time)
          GPIO.output(B, False)
          GPIO.output(C, False)

      def Step5():
          GPIO.output(B, True)
          sleep (time)
          GPIO.output(B, False)

      def Step6():
          GPIO.output(A, True)
          GPIO.output(B, True)
          sleep (time)
          GPIO.output(A, False)
          GPIO.output(B, False)

      def Step7():
          GPIO.output(A, True)
          sleep (time)
          GPIO.output(A, False)

      def Step8():
          GPIO.output(D, True)
          GPIO.output(A, True)
          sleep (time)
          GPIO.output(D, False)
          GPIO.output(A, False)

      # Volle Umdrehung
      # da wir 4 magneten haben, brauchen wir 8 Schritte
      # 512 schritte sind eine 45 grad umdrehung;   512/8=64
      #90vor
      for i in range (128):
          Step1()
          Step2()
          Step3()
          Step4()
          Step5()
          Step6()
          Step7()
          Step8()
          print i
      #90zurueck
      for i in range (128):
          Step8()
          Step7()
          Step6()
          Step5()
          Step4()
          Step3()
          Step2()
          Step1()
          print i



      GPIO.cleanup()

if __name__ == "__main__":
   main(sys.argv[1:])

