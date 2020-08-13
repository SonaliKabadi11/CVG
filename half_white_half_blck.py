import cv2
import numpy as np

a= np.zeros((240,240))
a=np.uint8(a)
a[:,:120]=0
a[:,120:240]=255
cv2.imwrite('blue.png',a)
