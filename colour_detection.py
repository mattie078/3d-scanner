import cv2
import numpy as np

while(1):

    # Get image
    path = r'C:\Users\Matthijs\Desktop\input\input.jpg'
    frame = cv2.imread(path)

    # converting from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    
    mask_before = cv2.inRange(hsv, lower_red, upper_red)
    mask_after = cv2.bitwise_not(mask_before)
 
    res1 = cv2.bitwise_and(frame,frame,mask=mask_before)
    res2 = cv2.bitwise_and(frame,frame,mask=mask_after)

    cv2.imshow("result1",res1)
    cv2.imshow("result2",res2)
    cv2.waitKey(1)