import cv2
import numpy as np

a=np.zeros((240,240))
a=np.uint8(a)

a[:240//3,:]=0
a[240//3:2*(240//3),:]=127
a[2*(240//3):240,:]=255
cv2.imwrite('3colors.png',a)

    