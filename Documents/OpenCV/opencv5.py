import cv2
from cv2 import CV_32FC1 

cap = cv2.VideoCapture(0)
mog = cv2.createBackgroundSubtractorMOG2()
while True:
    _, frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow("Video2", fgmask)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", gri)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()