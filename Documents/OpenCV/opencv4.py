import cv2



img = cv2.imread(r"E:\Projelerim\cisco_202200314\Documents\OpenCV\3.jpeg") # opencv dosyasının yolunu belirtiyoruz
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th =  cv2.threshold(gri, 127, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Ekran", th)
cv2.imshow("Image", img) # resim ekrana yazdırılır
cv2.waitKey(0) # ekrana yazdırılırken bekleme süresi
cv2.destroyAllWindows() # ekranda kalan pencereleri kapatır