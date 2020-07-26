from skimage.io import imshow, imread, imsave 
from skimage import img_as_float, img_as_ubyte
img = imread('img.png')
img_f = img_as_float(img)
r = img_f[:, :, 0]
g = img_f[:, :, 1]
b = img_f[:, :, 2]
img_rez = 0.2126*r+0.7152*g+0.0722*b
img_int = img_as_ubyte(img_rez)
imsave('out_img.png', img_int)
