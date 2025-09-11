import cv2
import numpy as np
img = cv2.imread('sources/ir.jpeg')
cv2.namedWindow('image')

for j in range(100):
  for i in range(100):
    img[100 + j, 100 + i, 2] = 255

while(1):
  cv2.imshow('image', img)
  k=cv2.waitKey(1)&0xFF
  if k==27:
    break

cv2.destroyAllWindows()