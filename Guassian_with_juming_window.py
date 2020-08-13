# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:50:13 2020

@author: Sonali Kabadi
Program: Guassian filter with jumping window
"""



import cv2
import numpy as np
I= cv2.imread('C:/Users/HP/Desktop/b.png',0)

patch = [[1,2,1],[2,4,2],[1,2,1]]
patch = np.array(patch)

patch_size = [3,3]
s = I.shape
upper_limit = s[0]//patch_size[0]
lower_limit = s[1]//patch_size[1]

op_matrix = np.zeros([s[0]-2,s[1]-2])

for i in range(0,upper_limit):
    for j in range(0,lower_limit):
        op=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                op[k,l]=I[i*patch_size[0]+k,j*patch_size[1]+l]
        temp = np.sum(patch*op)
        temp = temp/16
        op_matrix[i,j] = temp
        
op_matrix = np.uint8(op_matrix)
cv2.imshow('output0.png',op_matrix)
cv2.waitKey(0)