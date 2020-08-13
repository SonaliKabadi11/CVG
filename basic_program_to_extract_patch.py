import numpy as np
A=np.ones([10,10])
counter=1
for i in range (10):
    for j in range (10):
        A[i,j]=counter
        counter=counter+1
patch_size=[3,3]
size_A=A.shape

inp1=int(input("Enter row(0-8)   "))
inp2=int(input("Enter colomn(0-8)    "))

i=inp1*3
j=inp2*3

output=np.zeros(patch_size)
for k in range (patch_size[0]):
    for m in range (patch_size[1]):
        output[k,m]=A[i+k,j+m]

print(output)