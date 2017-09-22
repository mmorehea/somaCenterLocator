#code.interact(local=dict(globals(), **locals())) 


from scipy import misc
import glob
import code
from PIL import Image
import numpy as np
import sys
from matplotlib import pyplot as plt

image_path = ".//s8//Cell_0390.png"
img = misc.imread(image_path)


# TOP LEFT

subimg = img[100:800, 94:869, :]

xx,yy,zz = subimg.shape

subimg[90, :, :] = [255,0,0] # upper left corner
subimg[xx-50, :, :] = [0,255,0] # lower right corner

showimg = Image.fromarray(subimg, 'RGB')
showimg.show()

white = np.where(subimg == [255, 255, 255])
black = np.where(subimg == [0, 0, 0])
blue = np.where(subimg == [0, 0, 255])

mask = np.ones(subimg.shape)
mask[white] = 0
mask[black] = 0
mask[blue] = 0

mask = mask[:,:,0]
mask *= 255
dot = np.where(mask == 255)

XZlong = (np.max(dot[1]) + np.min(dot[1])) / 2
XZlat = (np.max(dot[0]) + np.min(dot[0])) / 2

#code.interact(local=dict(globals(), **locals()))

mask[int(XZlat), int(XZlong)] = 155

showimg = Image.fromarray(mask)
showimg.show()

# ----------------------------------------------



subimg = img[100:800, 1050:1700, :]

xx,yy,zz = subimg.shape

subimg[108, :, :] = [255,0,0] 
subimg[xx-45, :, :] = [255,0,0] 

subimg[:, 44, :] = [255,0,0] 
subimg[:, yy-37, :] = [255,0,0] 


showimg = Image.fromarray(subimg, 'RGB')
showimg.show()


white = np.where(subimg == [255, 255, 255])
black = np.where(subimg == [0, 0, 0])
blue = np.where(subimg == [0, 0, 255])

mask = np.ones(subimg.shape)
mask[white] = 0
mask[black] = 0
mask[blue] = 0

mask = mask[:,:,0]
mask *= 255
dot = np.where(mask == 255)

YZlong = (np.max(dot[1]) + np.min(dot[1])) / 2
YZlat = (np.max(dot[0]) + np.min(dot[0])) / 2

# code.interact(local=dict(globals(), **locals()))

mask[int(YZlat), int(YZlong)] = 155

showimg = Image.fromarray(mask)
showimg.show()



code.interact(local=dict(globals(), **locals()))






#FOR BOTTOM LEFT GRAPH

subimg = img[1072:1600, 94:869, :]

xx,yy,zz = subimg.shape

subimg[3, 38, :] = [255,0,0]  #upper left corner
subimg[xx-3, yy-38, :] = [0,255,0] #lower right corner

showimg = Image.fromarray(subimg, 'RGB')
showimg.show()

white = np.where(subimg == [255, 255, 255])
black = np.where(subimg == [0, 0, 0])
blue = np.where(subimg == [0, 0, 255])

mask = np.ones(subimg.shape)
mask[white] = 0
mask[black] = 0
mask[blue] = 0

mask = mask[:,:,0]
mask *= 255
dot = np.where(mask == 255)

long = (np.max(dot[1]) + np.min(dot[1])) / 2
lat = (np.max(dot[0]) + np.min(dot[0])) / 2

code.interact(local=dict(globals(), **locals()))

mask[int(lat), int(long)] = 155



showimg = Image.fromarray(mask)
showimg.show()


# code.interact(local=dict(globals(), **locals())) 
