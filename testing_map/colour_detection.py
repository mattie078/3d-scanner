import cv2
import numpy as np
import imutils
from picamera import PiCamera

class getContours(object):
    
    def __init__(self):

        self.X=[]
        self.Y=[]
        self.redlow=240
        self.redup=255
        self.greenlow=150
        self.greenup=255
        self.bluelow=150
        self.blueup=255
        self.camera = PiCamera()

    def calculateContour(self):

        self.cap = cv2.VideoCapture(0)
        _, self.frame = self.cap.read()
        print(self.frame.shape)
        #self.path = r'test.jpg'
        #self.frame = cv2.imread(self.path) #Read the video device input
		#self.frame = cv2.flip(self.frame, 1) #This should be uncommented to get the mirror image of the actual frame
        #self.frame = self.camera.capture('foo.jpg')
        #cv2.imwrite("input.jpg", self.frame)
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        self.lower = np.array([self.bluelow,self.greenlow,self.redlow]) #lower limit of BGR values of the laser line
        self.upper= np.array([self.blueup,self.greenup,self.redup]) #upper limit of BGR values of the laser line
        self.mask = cv2.inRange(self.hsv, self.lower, self.upper) #create a mask within the specified values of RED
        self.output_img = self.frame.copy() #a copy of the main frame is created
        self.output_img[np.where(self.mask==0)] = 0 #where the mask value is 0, make those coordinates black
        self.output_img[np.where(self.mask>100)] =255 #The target points, or the points which belong to the laser line are displayed in white
        self.gray = cv2.cvtColor(self.output_img, cv2.COLOR_BGR2GRAY)
        self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
        self.thresh = cv2.threshold(self.gray, 45, 255, cv2.THRESH_BINARY)[1]
        self.thresh = cv2.erode(self.thresh, None, iterations=2)
        self.thresh = cv2.dilate(self.thresh, None, iterations=2)

        self.cnts = cv2.findContours(self.thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        self.cnts = self.cnts[0] if imutils.is_cv2() else self.cnts[1]

        for i in range(len(self.cnts)):
                self.c=self.cnts[i]
                cv2.drawContours(self.output_img, [self.c], -1, (0, 255, 255), 2) #Draw all the contours with a red background
        cv2.imwrite("output.jpg", self.output_img)

def main():
    my_obj = getContours()
    my_obj.calculateContour() 

if __name__ == "__main__":
    main()
