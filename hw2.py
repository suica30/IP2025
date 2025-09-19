import cv2
import numpy as np
cap = cv2.VideoCapture('sources/sky.avi')

# rgb(175, 218, 190)
# rgb(190, 244, 227)
# rgb(166, 172, 124)

while(cap.isOpened()):
  ret, frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  lower_blue = np.array([30,40,40])
  upper_blue = np.array([180,255,255])
  mask = cv2.inRange(hsv, lower_blue, upper_blue)
  res = cv2.bitwise_and(frame, frame, mask=mask)
  cv2.imshow('frame', frame)
  cv2.imshow('mask', mask)
  cv2.imshow('res', res)

  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break
  
cv2.destroyAllWindows()