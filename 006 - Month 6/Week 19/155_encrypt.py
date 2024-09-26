# Made this for my CIS 155 class

from PIL import Image
from PIL.ExifTags import TAGS

with Image.open('cr.gif') as img:
    img.info['comment'] = "CIS 155!"
    img.save('output.gif')
