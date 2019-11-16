from Coordinates import Coordinates
from PixelsToMm import PixelsToMm
from Integratie import Integratie
import time

#from Motor import Motor

def main():
    #MotorObject = Motor()
    
    #Coordinates.calculate_coordinates(0)
    PixelsToMm.calculate_real_distances(0)
    Integratie.ReadFile(0)

if __name__ == "__main__":
    start_time = time.clock()
    main()
    print("--- %s seconds ---" % (time.clock() - start_time)) 
