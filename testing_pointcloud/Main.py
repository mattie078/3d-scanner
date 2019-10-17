from Coordinates import Coordinates
from Intergration import Intergration

def main():

    #Coordinates.calculateCoordinates()
    Temp = Intergration()
    Intergration.ReadFile(Temp)
    Intergration.CalculateXYZ(Temp)

if __name__ == "__main__":
    main()