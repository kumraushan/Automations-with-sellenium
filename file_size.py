import urllib.request
import os
import time
import io
from PIL import Image
import PIL
import os
import glob



url = "https://firebasestorage.googleapis.com/v0/b/putatoeapp/o/Tshirt%2F1231599646909148?alt=media&token=54009ec2-e76b-4659-a9ff-15ca9701c3d6"
path = (urllib.request.urlopen(url).read())
size = (float(len(path))/1000)
print(size)
im = Image.open(io.BytesIO(path))
print(f"The image size dimensions are: {im.size}")
rgb_im = im.convert('RGB')
file_name = ("/home/raushan/Desktop/making_automations/putatoe_images/putatoe.jpg")
rgb_im.save(file_name, optimize=True, quality=50)
print(rgb_im.size)
# print(rgb_im.tell())
