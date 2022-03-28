import cv2
from cv2 import bilateralFilter
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    ############ resize ############
    yuzde = 40
    en = int(frame.shape[1]*yuzde/100)
    boy = int(frame.shape[0]*yuzde/100)
    boyut = (en,boy)
    frame = cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)
    ############ resize #####################
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original',frame)
    cv2.imshow('Gri',gri)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()