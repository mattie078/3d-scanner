import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BCM)

    ControlPin = [6,13,19,26]

    for pin in ControlPin:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)

    seq = [[1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1],
           [1,0,0,1],
           [1,0,0,0]]
    #ismahaan!!!!!!!!

    for i in range(512):
        for halfstep in range(9):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq[halfstep][pin])
                time.sleep(0.0001)
                print("DRAAIEN!!!!")
            
except:
    print('hallo')
    
finally:
    GPIO.cleanup()