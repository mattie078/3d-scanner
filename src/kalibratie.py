from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(1)
camera.capture('/home/pi/Desktop/3d-scanner/Fotos/testdistance.jpg')
time.sleep(1)
