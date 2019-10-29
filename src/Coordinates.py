import cv2
import numpy as np

class Coordinates():
    
    def calculateCoordinates():
        # Pakt de fotos die net zijn gemaakt
        path = r'test.jpg'
        image = cv2.imread(path)

        # Zet de fotos om in HSV formaat voor verdere bewerking
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
        lower_red = np.array([150, 150, 80])
        upper_red = np.array([255, 255, 255])

        # Maakt een mask die tussen de 2 waardes hierboven zit
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Voegt de mask toe aan de fotos. Nu moeten we alleen de rode gebieden zien
        new_image = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Kijkt en slaat de pixels op in xycoordinates die wit zijn 
        indices = np.where(new_image == [255])

        coordinates = list(zip(indices[0], indices[1]))
        coordinatesNoDupes = []

        for index in coordinates:
            if index not in coordinatesNoDupes:
                coordinatesNoDupes.append(index)

        zipped_list = coordinatesNoDupes[:]
        np.savetxt('xycoordinates.txt', zipped_list, fmt = '%d')