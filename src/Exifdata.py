from picamera import PiCamera
from PIL import Image
from PIL.ExifTags import TAGS
import time
camera = PiCamera()
camera.capture('/home/pi/Desktop/3d-scanner/Fotos/feest.jpg')
time.sleep(5)
img = Image.open('/home/pi/Desktop/3d-scanner/Fotos/feest.jpg')
exif_data = img._getexif()
for tag, value in exif_data.items():
    print (TAGS.get(tag, tag), value)