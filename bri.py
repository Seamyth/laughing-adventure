import cv2
import numpy as np


cap = cv2.VideoCapture(0)
value = 35

while True:
    ret, grey = cap.read()
    
    grey_new = np.where((255 - grey) < value,255,grey+value)


    hsv = cv2.cvtColor(grey,cv2.COLOR_BGR2HSV)

    h,s,v = cv2.split(hsv)

    v = v + 10

    hsv = cv2.merge((h,s,v))

    hsv = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    
    res = np.hstack((hsv, grey_new))

    cv2.imshow('image', res)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
    
cv2.destroyAllWindows()
cap.release()
