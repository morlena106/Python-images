from skimage.io import imread, imshow, imsave
import numpy as np
img_n = imread('img.png')
l = 0
v = 0 
p = 0
n = 0 
test = img_n[0,0]
sh_sr = img_n.shape[0]//2
dl_sr = img_n.shape[1]//2
for i in range (dl_sr):
    if np.array_equal(img_n[sh_sr,i], test):
        l+=1
    if np.array_equal(img_n[sh_sr,img_n.shape[1]-i-1], test):
        p+=1
for i in range (sh_sr):
    if np.array_equal(img_n[i,dl_sr,], test):
        v+=1
    if np.array_equal(img_n[img_n.shape[0]-i-1,dl_sr], test):
        n+=1
print(l,v,p,n)
