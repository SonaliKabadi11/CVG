import cv2
import numpy as np

a=np.ones((240,240,3))
a=np.uint8(a)
for i in range (a.shape[0]):
    for j in range (a.shape[1]):
        if i>=j and i+j+1>=a.shape[1]:
            a[i,j,:]=0
        elif i<j and i+j+1>=a.shape[1]:
            a[i,j,2]=255
            a[i,j,0]=255
        elif i>j:
            a[i,j,1]=255
            a[i,j,2]=255
        else:
             a[i,j,0]=255
             a[i,j,1]=255
cv2.imshow('12345.png',a)

cv2.waitKey(0)










