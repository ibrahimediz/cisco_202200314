import cv2



img = cv2.imread(r"E:\Projelerim\cisco_202200314\Documents\OpenCV\3.jpeg") # opencv dosyasının yolunu belirtiyoruz

cv2.line(img,(0,0),(150,150),(255,255,255),15) # (img, p1, p2, color, thickness)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5) # (img, p1, p2, color, thickness)
cv2.circle(img,(100,63),55,(0,0,255), -1)# (img, center, radius, color, thickness)
cv2.putText(img,"OpenCV",(10,500),cv2.FONT_HERSHEY_COMPLEX,5,(255,255,255),10,cv2.LINE_AA) # (img, text, org, fontFace, fontScale, color, thickness, lineType)
cv2.imshow("Image", img) # resim ekrana yazdırılır
cv2.waitKey(0) # ekrana yazdırılırken bekleme süresi
cv2.destroyAllWindows() # ekranda kalan pencereleri kapatır
