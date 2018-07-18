import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image read
img = cv2.imread('testimg.jpg')
# b,g,r = cv2.split(img)
# img = cv2.merge([r,g,b])
# plt.imshow(img)
# plt.show()

# img1 = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# while(True):
#     cv2.imshow('cv2.imshow', img)
#     if(cv2.waitKey(0)):
#          cv2.destroyAllWindows()
#          break

#Image Write
# cv2.imwrite('saveImg-bg1.png',img[0:500,0:500])

#Image size
#h,w,c = img.shape
# sizeV = img.shape
# print(sizeV)
#print("The image is {} * {}* {}".format(h,w,c) )

# http://www.cnblogs.com/Matrix420/p/4204442.html
# http://matplotlib.org/examples/color/colormaps_reference.html
# http://matplotlib.org/users/image_tutorial.html
# http://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/
# color space

b,g,r = cv2.split(img)
image_hue_saturation_value = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(image_hue_saturation_value)
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(2)
plt.subplot(231), plt.imshow(r, cmap = "Accent"), plt.title('RED')
plt.subplot(232), plt.imshow(g, cmap = "Accent"), plt.title('GREEN')
plt.subplot(233), plt.imshow(b, cmap = "Accent"), plt.title('BLUE')
plt.subplot(234), plt.imshow(h, cmap = "Accent"), plt.title('HUE')
plt.subplot(235), plt.imshow(s, cmap = "Accent"), plt.title('SATURATION')
plt.subplot(236), plt.imshow(v, cmap = "Accent"), plt.title('VALUE')
plt.show()
plt.figure(3)
plt.subplot(231),plt.imshow(r, cmap = "gray"),plt.title('RED')
plt.subplot(232),plt.imshow(g, cmap = "gray"),plt.title('GREEN')
plt.subplot(233),plt.imshow(b, cmap = "gray"),plt.title('BLUE')
plt.subplot(234),plt.imshow(h, cmap = "gray"),plt.title('HUE')
plt.subplot(235),plt.imshow(s, cmap = "gray"),plt.title('SATURATION')
plt.subplot(236),plt.imshow(v, cmap = "gray"),plt.title('VALUE')
plt.show()

#image pixel operation
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

px = img[100, 100]
print(px)
blue = img[100,100,0]
print(blue)
img[100,100] = [255,255,255]
print(img[100, 100])



