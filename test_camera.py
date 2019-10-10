import cv2
import numpy as np

# Get image
path = r'test.jpg'
image = cv2.imread(path)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
         
lower_red = np.array([150,150,80])
upper_red = np.array([255,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)

new_image = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
print(new_image.shape)

sought = [255,255,255]

indices = np.where(new_image == [255])
coordinates = list(zip(indices[0], indices[1]))

zipped_list = coordinates[:]
print(len(zipped_list))

#result = np.count_nonzero(np.all(new_image==sought,axis=2))
#print(result)

# cv2.imshow("hsv", hsv)
# cv2.imshow("gray", new_image)