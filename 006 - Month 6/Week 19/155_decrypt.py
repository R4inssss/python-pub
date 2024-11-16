# Decryption portion
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('output.gif')
print(img.info['comment'])
