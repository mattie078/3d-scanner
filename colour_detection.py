import cv2
import numpy as np

while(1):

    # Get image
    path = r'test.jpg'
    frame = cv2.imread(path)

    # converting from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range
    lower_red = np.array([150,150,80])
    upper_red = np.array([255,255,255])
    
    mask_before = cv2.inRange(hsv, lower_red, upper_red)
    mask_after = cv2.bitwise_not(mask_before)
 
    res1 = cv2.bitwise_and(frame,frame,mask=mask_before)
    res2 = cv2.bitwise_and(frame,frame,mask=mask_after)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (5, 5), 0) 
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1] 
    thresh = cv2.erode(thresh, None, iterations=2) 
    thresh = cv2.dilate(thresh, None, iterations=2)

    cv2.imshow("original",frame)
    cv2.imshow("result1",res1)
    cv2.imshow("thresh",thresh)
    # cv2.imshow("result2",res2)
    
    cv2.waitKey(1)
    
