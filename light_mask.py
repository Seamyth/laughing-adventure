import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('frame',frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h,s,v = cv2.split(hsv)
    v = v + 10
    final_hsv = cv2.merge((h,s,v))

    img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)

    cv2.imshow("processed",img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
