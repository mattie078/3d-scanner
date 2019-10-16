import numpy as np
import cv2

class Filter:
#    def colorDetection(self, m):
	 for n in range(0,72):
		image = cv2.imread('/home/pi/Desktop/3d-scanner/Fotos/test' + str(n) + '.jpg')
        	
		hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
         	
		lower_red = np.array([253,245,245])
		upper_red = np.array([255,255,255])

		mask = cv2.inRange(hsv,lower_red,upper_red)
        	
        	
		cv2.imwrite('/home/pi/Desktop/3d-scanner/FotosHSV/filter' +str(n)+'.jpg', mask)
