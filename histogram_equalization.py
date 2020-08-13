import cv2
import numpy as np

A=cv2.imread('C:/Users/HP/Desktop/a.png',0)
a=A.shape
hist=np.zeros(256)
for i in range (a[0]):
    for j in range (a[1]):
        hist[A[i,j]]+=1
import matplotlib.pyplot as plt
plt.plot(hist)

ch=np.zeros(256)
for i in range (len(hist)):
    if i==0:
        ch[i]=hist[i]
    else:
        ch[i]=hist[i]+ch[i-1]
        
for i in range (len(ch)):
    if ch[i]!=0:
        m=i
        break


LT=np.zeros(256)
for k in range (m,256):
    LT[k]=(ch[k]-ch[m])/(ch[255]-ch[m])
LT=LT*255
I=np.uint8(np.zeros((a[0],a[1])))
for i in range (a[0]):
    for j in range (a[1]):
        I[i,j]=LT[A[i,j]]

#cv2.imwrite('hist.png',I)
cv2.imshow('hist.png',I)       
cv2.waitKey(0)

histnew=np.zeros(256)
for i in range (a[0]):
    for j in range (a[1]):
        histnew[I[i,j]]+=1
plt.plot(histnew)
      