from Coordinates import Coordinates
from Intergration import Intergration

def main():

    for i in range(73):
        Coordinates.calculateCoordinates(i)
        Temp = Intergration()
        Intergration.ReadFile(Temp, i)
        Intergration.CalculateXYZ(Temp)

if __name__ == "__main__":
    main()