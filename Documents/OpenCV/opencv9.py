import cv2
import numpy as np
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r"Documents\OpenCV\cascades\haarcascade_frontalface_default.xml")
while True:
    _,frame = cap.read() # [[[255,74,42],[255,74,42],[255,74,42]]]  
    ############ resize ############
    yuzde = 40
    en = int(frame.shape[1]*yuzde/100)
    boy = int(frame.shape[0]*yuzde/100)
    boyut = (en,boy)
    frame = cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA) 
    ############ resize #####################
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # [[45],[48]]
    ############ yuzu tespit etme ###############
    faces = face_cascade.detectMultiScale(gri,1.3,15)   # [(50,50,100,100),(100,100,150,150)]
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        eyes_cascade = cv2.CascadeClassifier(r"Documents\OpenCV\cascades\haarcascade_eye_tree_eyeglasses.xml")
        roi_gray = gri[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eyes_cascade.detectMultiScale(roi_gray,1.3,15)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('Original',frame)
    cv2.imshow('Gri',gri)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
