import sys
from PIL import Image 

im = Image.open("map_stenod.jpg")
pixels = im.load()

for i in range(0, 20): 
    print(pixels[i, 0])