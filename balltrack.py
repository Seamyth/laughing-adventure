from collections import deque
import numpy as np 
import imutils
import cv2

greenlower = (29,86,6)
greenupper = (64,255,255)
pts = deque(maxlen = 100)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    frame = imutils.resize(frame, width=600)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenlower, greenupper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts)>0:

        c = max(cnts,key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        radius = int(radius)

        if radius>10:
            cv2.circle(frame, center, radius, (0,255,255),2)

            cv2.circle(frame, center, 5, (0,0,255),-1)


    
    pts.appendleft(center)


    for i in range(1,len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue

        cv2.line(frame, pts[i-1], pts[i],(0,0,255), 10 )

        

    cv2.imshow('Frame', frame)







cv2.destroyAllWindows()
camera.release()
