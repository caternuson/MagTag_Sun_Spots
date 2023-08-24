# Process SDO HMI image for display on MagTag
# Grab image first using:
#   wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_512_HMII.jpg -O spots.jpg

from PIL import Image, ImageEnhance

def lut(x):
    IN1 = 30
    IN2 = 80
    IN3 = 100

    OUT1 = 63
    OUT2 = 127
    OUT3 = 191
    OUT4 = 255
    if x < IN1:
        return OUT1
    elif x < IN2:
        return OUT2
    elif x < IN3:
        return OUT3
    else:
        return OUT4

img = Image.open("spots.jpg").convert("L")
img = img.crop( (45, 167, 466, 349) )
img = img.resize( (296, 128) )

img = img.point(lut)
#img = ImageEnhance.Brightness(img).enhance(1.5)
#img = ImageEnhance.Contrast(img).enhance(10)

img = img.convert("P", palette=Image.Palette.ADAPTIVE, colors=4)
img.save("out.bmp")
