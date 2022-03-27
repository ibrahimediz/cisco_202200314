import cv2
import numpy as np


img = cv2.imread(r"E:\Projelerim\cisco_202200314\Documents\OpenCV\3.jpeg") # opencv dosyasının yolunu belirtiyoruz
print(img.shape) # resmin boyutunu gösteriyoruz (960, 1280, 3)
img[100:200,100:200] = [255,255,255]
print(img[100:200,100:200])
cv2.imshow("Image", img) # resim ekrana yazdırılır
cv2.waitKey(0) # ekrana yazdırılırken bekleme süresi
cv2.destroyAllWindows() # ekranda kalan pencereleri kapatır
