import cv2
import numpy as np
from collections import deque
import imutils

cap = cv2.VideoCapture(0)

yellow_lower = np.array([22,60,200],np.uint8)
yellow_upper = np.array([60,255,255],np.uint8)


while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    frame = imutils.resize(frame, width = 600)

    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    kernal = np.ones((5,5),"uint8")

    yellow = cv2.dilate(yellow,kernal)

    
    mask_inv =  255 - kernal;
    final_im = mask_inv*kernal
    cv2.imshow('ldzjbf',final_im)
    
    cv2.imshow('asas',yellow)
    (ret, contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)

        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255),1)


    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    th3 = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    #th4 = cv2.cvtColor(th3,cv2.COLOR_GRAY2HSV)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    cv2.imshow('iamge',frame)
    cv2.imshow('thimage',th3)
    #cv2.imshow('reimage',th4)
    
cap.release()
cv2.destroyAllWindows()
