import cv2
import numpy as np


I= cv2.imread('C:/Users/HP/Desktop/b.png',0)

patch =[[-1,0,1],[-2,0,2],[-1,0,1]]
patch = np.array(patch)

patch_size = [3,3]
size_I = I.shape

op_matrix = np.zeros([size_I[0]-2,size_I[1]-2])

for i in range(0,size_I[0]-2):
    for j in range(0,size_I[1]-2):
        op=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                op[k,l]=I[i+k,j+l]
        temp = np.sum(patch*op)
        temp = temp/8
        op_matrix[i,j] = temp
        
op_matrix = np.uint8(op_matrix)
cv2.imwrite('C:/Users/HP/Desktop/output123.png',op_matrix)