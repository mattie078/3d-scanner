from Coordinates import Coordinates
from PixelsToMm import PixelsToMm
from Integratie import Integratie
#from Motor import Motor
import RPi.GPIO as GPIO
import cv2
import time

buttonPin = 10

pinRood = 36
pinBlauw = 40
pinGroen = 38

def rood():
    roodwaarde = (0 * 100) / 255
    groenwaarde = (0 * 100) / 255
    blauwwaarde = (255 * 100) / 255
 
    ROOD.ChangeDutyCycle(roodwaarde)
    GROEN.ChangeDutyCycle(groenwaarde)
    BLAUW.ChangeDutyCycle(blauwwaarde)

def groen():

    roodwaarde = (0 * 100) / 255
    groenwaarde = (255 * 100) / 255
    blauwwaarde = (0 * 100) / 255
 
    ROOD.ChangeDutyCycle(roodwaarde)
    GROEN.ChangeDutyCycle(groenwaarde)
    BLAUW.ChangeDutyCycle(blauwwaarde)

def waitForInput():
    groen()
    #print("Waiting on initial input...")
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            #print("Knop is ingedrukt!")
            rood()
            time.sleep(4)
            break   # Knop is ingedrukt

def main():
    #MotorObject = Motor()
    waitForInput()

    print("Starting")

    
    for i in range(73): # alleen voor debugging

        if GPIO.input(buttonPin) == GPIO.LOW:  # Force stop 
            break

        #Motor.turnMotor(MotorObject, i)
        #Coordinates.calculate_coordinates(0, i)

    #Integratie.ReadFile(0)

if __name__ == "__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(pinRood, GPIO.OUT)
    GPIO.setup(pinGroen, GPIO.OUT)
    GPIO.setup(pinBlauw, GPIO.OUT)

    ROOD = GPIO.PWM(pinRood, 1000)
    GROEN = GPIO.PWM(pinGroen, 1000)
    BLAUW = GPIO.PWM(pinBlauw, 1000)
    ROOD.start(0)
    GROEN.start(0)
    BLAUW.start(0)

    main()


