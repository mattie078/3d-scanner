from Coordinates import Coordinates
from PixelsToMm import PixelsToMm
from Integratie import Integratie
from Motor import Motor
import RPi.GPIO as GPIO
import cv2
import time

buttonPin = 10
ledPin = 12

def main():
    #MotorObject = Motor()
    waitForInput()

    print("Starting")

    
    for i in range(73): # alleen voor debugging

        if GPIO.input(buttonPin) == GPIO.HIGH:  # Force stop 
            break

        #Motor.turnMotor(MotorObject, i)
        #Coordinates.calculate_coordinates(0, i)

    #Integratie.ReadFile(0)

if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

    start_time = time.perf_counter()    # .clock() mag niet meer gebruikt te worden sinds Python3.3. dit doet hetzelfde.
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))

def waitForInput():
    GPIO.output(ledPin, GPIO.HIGH) #GROEN
    print("Waiting on initial input...")
    while True:
        if GPIO.input(buttonPin) == GPIO.HIGH:
            print("Ingedrukt!")
            GPIO.output(ledPin, GPIO.HIGH) #ROOD
            break   # Knop is ingedrukt
