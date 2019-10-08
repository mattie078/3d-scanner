import cv2
import numpy as np

# Get image
path = r'test.jpg'
image = cv2.imread(path)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
lower_red = np.array([150,150,80])
upper_red = np.array([255,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)
#cv2.imshow("hsv", mask)

print(mask.shape)

new_image = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
print(mask[526,400]) # [254 254 254]

sought = [94,133,218]

#image[np.where((image==[94,133,218]).all(axis=2))] = [255,255,255]

#result = np.count_nonzero(np.all(mask==sought,axis=2))
#print(result)
# cv2.waitKey(100000)
# cv2.destroyAllWindows()