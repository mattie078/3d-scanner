import cv2
import numpy as np
import imutils


class getContours(object):
    
    def __init__(self):

        # Get image
        #self.path = r'test.jpg'
        #self.frame = cv2.imread(self.path)

        # # converting from BGR to HSV color space
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # # Range
        # lower_red = np.array([150,150,80])
        # upper_red = np.array([255,255,255])
    
        # mask_before = cv2.inRange(hsv, lower_red, upper_red)
        # mask_after = cv2.bitwise_not(mask_before)
 
        # res1 = cv2.bitwise_and(frame,frame,mask=mask_before)
        # res2 = cv2.bitwise_and(frame,frame,mask=mask_after)

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        # gray = cv2.GaussianBlur(gray, (5, 5), 0) 
        # thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1] 
        # thresh = cv2.erode(thresh, None, iterations=2) 
        # thresh = cv2.dilate(thresh, None, iterations=2)

        self.X=[]
        self.Y=[]
        self.redlow=240
        self.redup=255
        self.greenlow=150
        self.greenup=255
        self.bluelow=150
        self.blueup=255

    def calculateContour(self):

        #VICEOCAPTURE INPUT
        self.cap = cv2.VideoCapture(0) #Video Device(webcam) is opened
        self.frame = self.cap.read()[1]

        self.lower = np.array([self.bluelow,self.greenlow,self.redlow]) 
        self.upper= np.array([self.blueup,self.greenup,self.redup]) 
        self.mask = cv2.inRange(self.frame, self.lower, self.upper) 
        self.output_img = self.frame() 
        self.output_img[np.where(self.mask==0)] = 0 
        self.output_img[np.where(self.mask>100)] =255 
        self.gray = cv2.cvtColor(self.output_img, cv2.COLOR_BGR2GRAY)
        self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
        self.thresh = cv2.threshold(self.gray, 45, 255, cv2.THRESH_BINARY)[1]
        self.thresh = cv2.erode(self.thresh, None, iterations=2)
        self.thresh = cv2.dilate(self.thresh, None, iterations=2)
    
	    #Finding the contours
        self.cnts = cv2.findContours(self.thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        self.cnts = self.cnts[0] if imutils.is_cv2() else self.cnts[1]

        for i in range(len(self.cnts)):
            self.c=self.cnts[i]
            cv2.drawContours(self.output_img, [self.c], -1, (0, 255, 255), 2)

        # cv2.imshow("original",frame)
        cv2.imwrite("output.jpg", output_img) 
        # cv2.imshow("result1",self.output_img)
        # cv2.imshow("thresh",thresh)
        # cv2.imshow("result2",res2)
    
def main():
    my_obj = getContours()
    my_obj.calculateContour() 

if __name__ == "__main__":
    main()