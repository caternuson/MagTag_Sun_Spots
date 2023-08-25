# MagTag_Sun_Spots
Display daily solar sun spot map on an [Adafruit MagTag](https://www.adafruit.com/product/4800).


# Data Source
The source image is taken from the Solar Dynamics Observatory [SDO](https://sdo.gsfc.nasa.gov/)
website. Specifically, the [512x512 HMI Intensitygram](https://sdo.gsfc.nasa.gov/assets/img/latest/latest_512_HMII.jpg).


# Code
There are two parts to the code:
  * `process_hmi.py` - This is to be run by Github Actions. The action downloads
     the latest image and processes it with the resulting output saved
     in the file out.bmp, which is then commited back to this repo.
  * `code.py` - This is to be run on the MagTag. It downloads out.bmp
     from this repository and displays it on the MagTag.


# Example
The resulting processed bitmap looks like:

![out.bmp](out.bmp "out.bmp")