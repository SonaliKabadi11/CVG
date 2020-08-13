# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:18:00 2020

@author: Sonali Kabadi
Program: Sobelv with jumping window
"""


import cv2
import numpy as np


I= cv2.imread('C:/Users/HP/Desktop/b.png',0)

patch =[[-1,0,1],[-2,0,2],[-1,0,1]]
patch = np.array(patch)

patch_size = [3,3]
size_I = I.shape
upper_limit = size_I[0]//patch_size[0]
lower_limit = size_I[1]//patch_size[1]
op_matrix = np.zeros([size_I[0]-2,size_I[1]-2])

for i in range(0,upper_limit):
    for j in range(0,lower_limit):
        op=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                op[k,l]=I[i*patch_size[0]+k,j*patch_size[1]+l]
        temp = np.sum(patch*op)
        temp = temp/8
        op_matrix[i,j] = temp
        
op_matrix = np.uint8(op_matrix)
cv2.imwrite('C:/Users/HP/Desktop/sobelv_jumping.png',op_matrix)
