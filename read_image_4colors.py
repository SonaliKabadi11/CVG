import cv2

import numpy as np


a=np.array(cv2.imread('C:/Users/HP/Desktop/a.png'))
k,l=a.shape[0],a.shape[1]

a[:k//2,:l//2,(1,2)]=0
a[:k//2,l//2:l,(0,1)]=0
a[k//2:k,:l//2,(0,2)]=0


#print(a.shape())
cv2.imshow('a1.png',a)
cv2.waitKey(0) 
