# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:53:01 2020

@author: Sonali Kabadi
program: medain filter with sliding window
"""
import cv2
import numpy as np
import random

I = cv2.imread('C:/Users/HP/Desktop/b.png',0)
I = np.array(I)
s = I.shape

for q in range (1000):
    x = random.randint(0,s[0]-1)
    y = random.randint(0,s[1]-1)
    I[x,y] = random.randint(0,1)*255
patch_size =[3,3]

output_matrix = np.zeros([s[0]-3,s[1]-3])

for i in range(0,s[0]-3):
    for j in range (s[1]-3):
        op=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range (patch_size[1]):
                op[k,l] = I[i+k,j+l]
        
        temp = np.median(op)
        output_matrix[i+1,j+1] = temp
        
cv2.imshow('out[ut1.png',output_matrix)
cv2.waitKey(0)
       
