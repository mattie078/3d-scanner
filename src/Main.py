from Integratie import Integratie
from Coordinates import Coordinates
import cv2

import time

#from Motor import Motor

def main():
    #MotorObject = Motor()

    for i in range(73): # alleen voor debugging
        Coordinates.calculate_coordinates(0, i)

    Integratie.ReadFile(0)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))
