#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

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

# Schritte 1 - 8 festlegen
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
# 4096 schritte sind eine 360 grad umdrehung; 4096/8=512
# 228 schritte sind eine 20 grad umdrehung;   228/8=28.5
# 512 schritte sind eine 45 grad umdrehung;   512/8=64
# 1024 schritte sind eine 90 grad umdrehung;   1024/8=128

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
