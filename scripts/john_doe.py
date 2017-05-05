#!/usr/bin/python3
import sys, os, getopt
import platform
import time
from time import sleep
from idlelib.tabbedpages import TabbedPageSet
from array import array

# check the architecture of the system for GPIO mode
if os.uname()[4][:3] == 'arm':
    import RPi.GPIO as GPIO
else:
    emulatorgui_path = os.path.abspath(os.path.join('..', 'emulatorgui'))
    sys.path.append(emulatorgui_path)
    from EmulatorGUI import GPIO

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


def Step1_Step8():
    steps = ['D', 'C', 'B', 'A']

    for x in range(len(steps)):
        print (steps[x-1],steps[x])
        if x==3:
            print (steps[0])
        else:
            print (steps[x])
        
        #GPIO.output(gpio_steps.B, True)
        #GPIO.output(gpio_steps.C, True)
        #sleep (gpio_steps.time)
        #GPIO.output(gpio_steps.B, False)
        #GPIO.output(gpio_steps.C, False)

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



def move(organ):
    if organ == 'head':
        # Verwendete Pins(GPIP) am Rapberry Pi
        A=22
        B=23
        C=24
        D=25
        time = 0.0010
      
        gpio_steps(A,B,C,D,2) 
        print ('move',organ)
         
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
            
        GPIO.cleanup()
    elif organ == 'eyes':
        # Verwendete Pins(GPIP) am Rapberry Pi
        A=6
        B=12
        C=13
        D=5
        time = 0.0010
          
        gpio_steps(A,B,C,D,2) 
        print ('move',organ)
    
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
        print ('move',organ)
    
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


def blink(color,duration):
    # Verwendete Pins(GPIP) am Rapberry Pi
    if color == 'red':
       gpio_color=17
    elif color == 'green':
       gpio_color=18
    elif color == 'blue':
       gpio_color=27

    GPIO.setup(gpio_color,GPIO.OUT)
    
    print ("LED", color, "on")
    GPIO.output(gpio_color,GPIO.HIGH)
    time.sleep(float(duration))
   
    print ("LED", color, "off")
    GPIO.output(gpio_color,GPIO.LOW)

    GPIO.cleanup()
    
    
def speak(words):
    print (words)


def play(song):
    print ('play', song)
    
    
###########################################
############### MAIN CLASS ############### 
###########################################
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ha:o:c:d:",["action=:organ=:color=:duration="])
    except getopt.GetoptError:
        print ('john_doe -a <action> [-o <organ>] [-c <color>] [-d <duration>] [-w <words>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('john_doe -a <action> [-o <organ>]')
            sys.exit()
        elif opt in ("-a", "--action"):
            action = arg  
        elif opt in ("-o", "--organ"):
            organ = arg
        elif opt in ("-c", "--color"):
            color = arg
        elif opt in ("-d", "--duration"):
            duration = arg
        elif opt in ("-w", "--words"):
            words = arg
        elif opt in ("-s", "--song"):
            song = arg
            

    if action == 'move':
        if 'organ' not in locals():
            print ('Error: organ is missing')
            exit()
        else:
            move(organ)
    elif action == 'blink':
        if 'color' not in locals():
            print ('Error: color is missing')
            exit()
        else:
            if 'duration' not in locals():
                # set default sec for LED duration
                duration=2
            blink(color,duration)
    elif action == 'speak':
        if 'words' not in locals():
            print ('Error: words is missing')
            exit()
        else:
            speak(words)
    elif action == 'play':
        if 'song' not in locals():
            print ('Error: song is missing')
            exit()
        else:
            play(song)
    elif action == 'diagnostic':
        words="Hello, my name is John Doe."
        song="klassenfahrt"
        
        move('head')
        move('eyes')
        move('jaw')
        
        blink('red','2')
        blink('green','2')
        blink('blue','2')
        
        speak(words)
        
        play(song)


if __name__ == "__main__":
   main(sys.argv[1:])

