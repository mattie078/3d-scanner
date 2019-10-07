import numpy as np
import cv2

class Filter:
    def colorDetection(self, m):
        image = cv2.imread('/home/pi/Desktop/Fotos/test' + str(m) + '.jpg')

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
        lower_red = np.array([150,150,80])
        upper_red = np.array([255,255,255])

        mask = cv2.inRange(hsv,lower_red,upper_red)

        cv2.imwrite('FotosHSV/filer' +str(m)+'.jpg', mask)
