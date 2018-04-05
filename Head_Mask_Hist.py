import cv2
import numpy as np
from collections import deque
import imutils

cap = cv2.VideoCapture(0)

yellow_lower = np.array([22,60,200],np.uint8)
yellow_upper = np.array([60,255,255],np.uint8)


while True:
    ret, frame = cap.read()

    if ret == False:
        break
        
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame = imutils.resize(frame, width = 600)

    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)


    (ret, contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)

        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (107,214,233),1)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    cv2.imshow('Headlight detection',frame)
    
    #Histogram equalization
    
    bgr = frame

    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

    lab_planes = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

    lab_planes[0] = clahe.apply(lab_planes[0])

    lab = cv2.merge(lab_planes)

    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    cv2.imshow('Histogram Equalized',bgr)


    ##Masking preliminary

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    v = v + 10
    s = s + 5
    final_hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow("Masking",img)

    
    
cap.release()
cv2.destroyAllWindows()
