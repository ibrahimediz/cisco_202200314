"""
Dosya açmak için sürekli kullanabileceğimiz bir fonksiyon yazalım
"""
import os 
def open_file(file_path,ar=0):
    mode = "r+"
    if os.path.exists(file_path):
        if ar==1:
            mode = "a+"
        else:
            mode = "r+"
    else:
        if ar==1:
            mode = "x+"
        else:
            mode = "w+"
    return open(file_path,mode,encoding="utf-8")

"""
write fonksiyonu dosyaya yazmak için kullanılır
writeline fonksiyonu bir satır yazmak için kullanılır
writelines fonksiyonu bir liste yazmak için kullanılır
"""

dosya1 = open_file(r"FileOperations\file.csv")
okunan = dosya1.readlines()[:5]
print(okunan)
dosya2 = open_file(r"FileOperations\file2.csv")
dosya2.writelines(okunan)
dosya1.close()
dosya2.close()
