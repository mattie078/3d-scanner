import cv2
import numpy as np
import imutils


class getContours(object):
    
    def __init__(self):

        self.X=[]
        self.Y=[]
        self.redlow=150
        self.redup=255
        self.greenlow=200
        self.greenup=255
        self.bluelow=200
        self.blueup=255

    def calculateContour(self):

        #Get image
        self.path = r'test.jpg'
        self.frame = cv2.imread(self.path)

        # converting from BGR to HSV color space
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv",self.hsv)

        # Range
        self.lower = np.array([0,50,50])
        self.upper = np.array([10,255,255])
            
        mask_before = cv2.inRange(self.hsv, self.lower, self.upper)
        mask_after = cv2.bitwise_not(mask_before)
 
        res1 = cv2.bitwise_and(self.frame,self.frame,mask=mask_before)
        res2 = cv2.bitwise_and(self.frame,self.frame,mask=mask_after)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        gray = cv2.GaussianBlur(gray, (5, 5), 0) 
        thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1] 
        thresh = cv2.erode(thresh, None, iterations=2) 
        thresh = cv2.dilate(thresh, None, iterations=2)
    
	    #Finding the contours
        self.cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        self.cnts = self.cnts[0] if imutils.is_cv2() else self.cnts[1]

        for i in range(len(self.cnts)):
            self.c=self.cnts[i]
            cv2.drawContours(res2, [self.c], -1, (0, 255, 255), 2)

        # cv2.imshow("original",frame)
        cv2.imwrite("output.jpg", res2) 
        # cv2.imshow("result1",self.output_img)
        # cv2.imshow("thresh",thresh)
        # cv2.imshow("result2",res2)
   
def main():
    my_obj = getContours()
    my_obj.calculateContour() 

if __name__ == "__main__":
    main()
