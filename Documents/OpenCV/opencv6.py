import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(frame,-1,kernel)
    blur = cv2.GaussianBlur(frame,(15,15),0)
    cv2.imshow('Original',frame)
    cv2.imshow('Smooth',smooth)
    cv2.imshow('Blur',blur)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


"""
# print(np.ones((5,5),np.uint8)/225)
# [[0.00444444 0.00444444 0.00444444 0.00444444 0.00444444]
#  [0.00444444 0.00444444 0.00444444 0.00444444 0.00444444]
#  [0.00444444 0.00444444 0.00444444 0.00444444 0.00444444]
#  [0.00444444 0.00444444 0.00444444 0.00444444 0.00444444]
#  [0.00444444 0.00444444 0.00444444 0.00444444 0.00444444]]
""" 