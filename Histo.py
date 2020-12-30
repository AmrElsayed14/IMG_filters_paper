import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./img/2.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.subplot(2,1,1)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('./img/equ_res.jpg',equ)
cv2.imwrite('./img/res.png',res)
#cdf2 = equ.cumsum()
#cdf_normalized2 = cdf2 * equ.max()/ cdf2.max()
plt.subplot(2,1,2)

#plt.plot(cdf_normalized2, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
#plt.legend('equalized histogram')
plt.show()
