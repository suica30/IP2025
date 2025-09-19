import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("sources/dataset/dsu2.jpg")
row,cols,ch = img.shape

pts1 = np.float32([
  (388, 248),
  (392, 497),
  (815, 507),
  (812, 230),
])

width = 400
height = int(400 * 249 / 424)

pts2 = np.float32([
  [0, 0],
  [0, height],
  [width, height],
  [width, 0]
])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(width,height))
plt.subplot(121),plt.imshow(img),plt.title("Input")
plt.subplot(122),plt.imshow(dst),plt.title("Output")
plt.show()
