import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
img = cv2.imread('sources/ir.jpeg')

isDown = False

mouse_x = 0
mouse_y = 0

cur_mouse_x = 0
cur_mouse_y = 0

mouse_down_x = 0
mouse_down_y = 0

def on_mouse(event, x, y, flags, param):
    global mouse_x, mouse_y, mouse_down_x, mouse_down_y, isDown, cur_mouse_x, cur_mouse_y
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_down_x = x
        mouse_down_y = y
        isDown = True
    elif event == cv2.EVENT_LBUTTONUP:
        isDown = False
    elif event == cv2.EVENT_MOUSEMOVE and isDown:
        cur_mouse_x = x
        cur_mouse_y = y
        mouse_x = x
        mouse_y = y
    elif event == cv2.EVENT_MOUSEMOVE:
        cur_mouse_x = x
        cur_mouse_y = y

cv2.namedWindow('image')
cv2.resizeWindow('image', 512, 300)

switch = 'value: ' 
cv2.createTrackbar(switch, 'image',0,255,nothing)
cv2.setMouseCallback('image',on_mouse)

while(1):
    img = cv2.imread('sources/ir.jpeg')
    
    if mouse_down_x != 0 and mouse_down_y != 0:
        start_y = min(mouse_down_y, mouse_y)
        start_x = min(mouse_down_x, mouse_x)
        end_y = max(mouse_down_y, mouse_y)
        end_x = max(mouse_down_x, mouse_x)
        r = cv2.getTrackbarPos(switch,'image')
        img[start_y:end_y, start_x:end_x, 2] = r
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'Mouse Position: '+str(cur_mouse_x)+','+str(cur_mouse_y),(10,30), font, 0.8,(255,255,255),2,cv2.LINE_AA)

    display_img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imshow('image', display_img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()