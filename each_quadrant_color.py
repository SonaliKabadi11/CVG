# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:41:11 2020

@author: HP
"""


import cv2
import numpy as np

a=np.ones((240,240,3))
a=np.uint8(a)  #initializing 8 bits to the image
a[:120,:120,0]=255
a[:120,120:240,1]=255
a[120:240,:120,2]=255
a[120:240,120:240,:]=255
cv2.imwrite('4colors.png',a)
#cv2.imshow('4colors.png',a)
#cv2.waitKey(0)