# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:46:58 2020

@author: Soanli Kabadi
Program: Median filter with jumping window
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
upper_limit = s[0]//patch_size[0]
lower_limit = s[1]//patch_size[1]


output_matrix = np.zeros([s[0]-3,s[1]-3])

for i in range(0,upper_limit):
    for j in range(0,lower_limit):
        op=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                op[k,l]=I[i*patch_size[0]+k,j*patch_size[1]+l]        
        temp = np.median(op)
        output_matrix[i+1,j+1] = temp
        
cv2.imshow('median_jumping_window.png',output_matrix)
cv2.waitKey(0)
       