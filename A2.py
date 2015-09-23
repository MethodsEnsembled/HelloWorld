import sys
from PIL import Image

def flip(img):
    width, height = img.size
    imgdup = img.copy()
    m = img.load()
    n = imgdup.load()

    for i in range(0,width):
        for j in range(0,height):
                m[i,j] = n[width-i-1,j]

    img.show()
    return img


__author__ = 'Bolun'
if len(sys.argv)<=1:
    print "missing image filename"
    sys.exit(1)
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img.convert("L")
# img.show()
flip(img)

