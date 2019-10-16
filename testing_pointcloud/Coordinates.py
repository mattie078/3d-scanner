import cv2
import numpy as np

class Coordinates():
    
    def calculateCoordinates():
        # Get image
        path = r'test.jpg'
        image = cv2.imread(path)

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
        lower_red = np.array([150, 150, 80])
        upper_red = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        new_image = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        indices = np.where(new_image == [255])

        coordinates = list(zip(indices[0], indices[1]))
        coordinatesNoDupes = []

        for index in coordinates:
            if index not in coordinatesNoDupes:
                coordinatesNoDupes.append(index)

        zipped_list = coordinatesNoDupes[:]
        np.savetxt('xycoordinates.txt', zipped_list, fmt = '%d')