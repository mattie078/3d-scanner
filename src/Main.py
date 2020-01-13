from Coordinates import Coordinates
from PixelsToMm import PixelsToMm
from Integratie import Integratie
from motor import Motor
from Calculations import Calculations
#from SaveToSD import SaveToSD
import RPi.GPIO as GPIO
import cv2
import time

buttonPin = 10

pinRood = 40
pinBlauw = 36
pinGroen = 38

def changeColor(color):
    if color == 'blue':
        roodwaarde = (0 * 100) / 255
        groenwaarde = (0 * 100) / 255
        blauwwaarde = (255 * 100) / 255
        
        ROOD.ChangeDutyCycle(roodwaarde)
        GROEN.ChangeDutyCycle(groenwaarde)
        BLAUW.ChangeDutyCycle(blauwwaarde)
    
    elif color == 'green':
        roodwaarde = (0 * 100) / 255
        groenwaarde = (255 * 100) / 255
        blauwwaarde = (0 * 100) / 255
 
        ROOD.ChangeDutyCycle(roodwaarde)
        GROEN.ChangeDutyCycle(groenwaarde)
        BLAUW.ChangeDutyCycle(blauwwaarde)

def waitForInput():
    changeColor('green')
    
    #print("Waiting on initial input...")
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            #print("Knop is ingedrukt!")
            changeColor('blue')
            break   # Knop is ingedrukt

def main():
    #MotorObject = Motor()
    CoordinatesObject = Coordinates()
    IntegratieObject = Integratie()
    CalculationsObject = Calculations()
    #SaveToSD_Object = SaveToSD()

    waitForInput()
    time.sleep(2)

    for i in range(73): # alleen voor debugging

        if GPIO.input(buttonPin) == GPIO.LOW:  # Force stop 
            print("Force stopping!")
            break

        #MotorObject.turnMotor(i)
        CoordinatesObject.calculate_coordinates(i)

    #IntegratieObject.ReadFile() NIET MEER GEBRUIKEN = OUD
    CalculationsObject.run()
    
    #PointCloud naar STL
    
    #Save to USB/SD
    #SaveToSD_Object.save()

if __name__ == "__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(pinBlauw, GPIO.OUT)
    GPIO.setup(pinGroen, GPIO.OUT)
    GPIO.setup(pinRood, GPIO.OUT)

    BLAUW = GPIO.PWM(pinBlauw, 1000)
    GROEN = GPIO.PWM(pinGroen, 1000)
    ROOD = GPIO.PWM(pinRood, 1000)
    ROOD.start(0)
    GROEN.start(0)
    BLAUW.start(0)

    main()


