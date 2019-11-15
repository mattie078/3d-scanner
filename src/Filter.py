import numpy as np
import cv2

class Filter:
    def colorDetection(self, m):
        image = cv2.imread('../Fotos/temp' + str(m) + '.jpg')
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
        lower_red = np.array([0, 0, 210])
        upper_red = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        cv2.imwrite('../FotosHSV/filter' +str(m)+'.jpg', mask)

    # for i in range(73):
    #     print("Masking photo " + str(i))
    #     colorDetection(0,i)
