from PIL import Image
from PIL.ExifTags import TAGS
img = Image.open('test.jpg')
exif_data = img._getexif()
# for tag, value in exif_data.items():
print (exif_data)
#