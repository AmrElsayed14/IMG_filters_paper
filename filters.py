import cv2
import numpy as np
from matplotlib import pyplot as plt

def box_kernel(img):
    plt.subplot(221),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    sizes = [41,81,121]
    for index,i in enumerate(sizes):
        blur = cv2.blur(img,(i,i))
        plt.subplot(2,2,index+2),plt.imshow(blur),plt.title('average Blurred')
        plt.xticks([]), plt.yticks([])

def Gaussian_filter(img):
    plt.subplot(221),plt.imshow(img),plt.title('Original 2')
    plt.xticks([]), plt.yticks([])
    sizes = [41,81,121]
    sigma = 7
    for index,i in enumerate(sizes):
        blur = cv2.GaussianBlur(img,(i,i),sigma)
        plt.subplot(2,2,index+2),plt.imshow(blur),plt.title('kernel size = '  + str(i) + ", " + "sigma = " + str(sigma))
        plt.xticks([]), plt.yticks([])

    


img = cv2.imread('./img/unnamed.jpg')

#blur = cv2.blur(img,(5,5))
#      |1 1 1 1 1|
# 1    |1 1 1 1 1|
# -- * |1 1 1 1 1|   this is averaging to get blur image 
# 25   |1 1 1 1 1|   and used for smoothing 
#      |1 1 1 1 1|


#box_kernel(img)
#plt.show()
Gaussian_filter(img)

#cv2.imwrite('./img/sigma0.jpg',)
plt.show()
