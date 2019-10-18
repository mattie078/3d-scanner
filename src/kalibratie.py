from picamera import PiCamera
import time

camera = PiCamera()
camera.capture('/home/pi/Desktop/3d-scanner/Fotos/afstandtest2.jpg')
time.sleep(1)