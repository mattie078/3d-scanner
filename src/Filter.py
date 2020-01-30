import numpy as np
import cv2


class Filter:
    # Haalt de gemaakte foto's door een filter. Alle felrode tot witte punten (waar de lasers dus op schijnen) worden
    # wit (#FFFFFF), de rest van de foto wordt zwart (#000000).
    def colorDetection(self, m):
        image = cv2.imread('../Fotos/temp' + str(m) + '.jpg')

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        upper_red = np.array([255, 255, 255])
        lower_red = np.array([40, 0, 100])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        cv2.imwrite('../FotosHSV/filter' + str(m) + '.jpg', mask)

    # for i in range(73):
    #     print("Masking photo " + str(i))
    #     colorDetection(0,i)
