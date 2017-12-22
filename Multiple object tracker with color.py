import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255],np.uint8)

    blue_lower = np.array([99,115,150],np.uint8)
    blue_upper = np.array([110,255,255],np.uint8)

    yellow_lower = np.array([22,60,200],np.uint8)
    yellow_upper = np.array([60,255,255],np.uint8)

    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    kernal = np.ones((5,5),"uint8")

    red = cv2.dilate(red,kernal)
    res = cv2.bitwise_and(img,img,mask=red)

    blue = cv2.dilate(blue,kernal)
    res1 = cv2.bitwise_and(img,img,mask=blue)

    yellow = cv2.dilate(yellow,kernal)
    res2 = cv2.bitwise_and(img,img,mask=yellow)

    #red
    (ret,contours,hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):

            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
            cv2.putText(img,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))

           
    #blue
    (ret,contours,hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):

            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
            cv2.putText(img,"blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))


 
    #yellow
    (ret,contours,hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):

            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x,y), (x+w,y+h), (60,255,255),2)
            cv2.putText(img,"YELLOW",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255))

    #showing result
    cv2.imshow('tracking color objcts',img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
cap.release()
