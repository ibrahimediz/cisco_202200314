import cv2
from cv2 import bilateralFilter
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    yuzde = 40
    en = int(frame.shape[1]*yuzde/100)
    boy = int(frame.shape[0]*yuzde/100)
    boyut = (en,boy)
    frame = cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)
    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(frame,-1,kernel)
    blur = cv2.GaussianBlur(frame,(15,15),0)
    mblur = cv2.medianBlur(frame,15)
    bilateralFilter = cv2.bilateralFilter(frame,15,75,75)
    cv2.imshow('Original',frame)
    cv2.imshow('Smooth',smooth)
    cv2.imshow('Blur',blur)
    cv2.imshow('Median Blur',mblur)
    cv2.imshow('Bilateral Filter',bilateralFilter)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()