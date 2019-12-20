from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from datetime import datetime
from Filter import Filter

class Motor:
    
    def __init__(self): 

        # Opent de camera om een foto te makenn
        self.camera = PiCamera()
        GPIO.setmode(GPIO.BOARD)
        self.ControlPin = [6,13,19,26]
        self.filterImage = Filter()
        # for pin in ControlPin:
        #     GPIO.setup(pin,GPIO.OUT)
        #     GPIO.output(pin,0)

        # Sequence om de motor juist te laten draaien
        self.seq = [[1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1],
            [1,0,0,0]]

        # Maakt 73 fotos (0 tot 72) en slaat deze op met de juiste benaming
        # Zet de filter op de foto

    def turnMotor(self,i):
        fotonaam = 'temp' + str(i) + ".jpg"
        self.camera.capture('/home/pi/Desktop/3d-scanner/Fotos/'+fotonaam)
        print(fotonaam)
        self.filterImage.colorDetection(i)
        for i in range(7):
            for halfstep in range(9):
                for pin in range(4):
                    GPIO.output(self.ControlPin[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        time.sleep(1)

        
