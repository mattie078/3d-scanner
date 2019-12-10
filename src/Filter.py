import numpy as np
import cv2
from Coordinates import Coordinates


class Filter:
    # Haalt de gemaakte foto's door een filter. Alle felrode tot witte punten (waar de lasers dus op schijnen) worden
    # wit (#FFFFFF), de rest van de foto wordt zwart (#000000).
    def colorDetection(self, m):
        image = cv2.imread('../Fotos/temp' + str(m) + '.jpg')
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
        lower_red = np.array([0, 0, 210])
        upper_red = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        cv2.imwrite('../FotosHSV/filter' +str(m)+'.jpg', mask)
        Coordinates.calculate_coordinates(0, m)    # linkt nu direct door.

    # for i in range(73):
    #     print("Masking photo " + str(i))
    #     colorDetection(0,i)
