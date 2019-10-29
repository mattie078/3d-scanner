from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from datetime import datetime
from Filter import Filter

class Motor:
    try:
        # Opent de camera om een foto te maken
        camera = PiCamera()
        GPIO.setmode(GPIO.BCM)
        ControlPin = [6,13,19,26]
        filter1 = Filter()
        for pin in ControlPin:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,0)

        # Sequence om de motor juist te laten draaien
        seq = [[1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1],
               [1,0,0,1],
               [1,0,0,0]]

        # Maakt 73 fotos (0 tot 72) en slaat deze op met de juiste benaming
        for m in range(73):
            fotonaam = 'test' + str(m) + ".jpg"
            camera.capture('/home/pi/Desktop/3d-scanner/Fotos/'+fotonaam)
            print(fotonaam)
            filter1.colorDetection(m)
            for i in range(7):
                for halfstep in range(9):
                    for pin in range(4):
                        GPIO.output(ControlPin[pin], seq[halfstep][pin])
                        time.sleep(0.001)
            time.sleep(1)
                    
    #except:
    #    print('mislukt')
        
    finally:
        GPIO.cleanup()
