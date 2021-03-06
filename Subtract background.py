import cv2
import numpy as np

cap = cv2.VideoCapture(0)

##for detecting moving objects and then we can use direclty fgbg instead of using this bulky,long thing
fgbg = cv2.createBackgroundSubtractorMOG2()


while True:
    ret, frame = cap.read()

    #applying on frame
    fgmask = fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    k = cv2.waitKey(10) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
