"""
Bir dosya nasıl açılır
"""
""" 
open("Dosyanın Adresi","Açma Modu","Karakter Seti")
"""
"""

# escape sequence \ ile dosya adresi belirtilir
"""
PATH = r"E:\Projelerim\FileOpProject\FileOperations\file.csv"
RELATIVE_PATH = r"FileOperations\file.csv"
# import pathlib as pt 
# print(pt.Path(RELATIVE_PATH).resolve())
# import os 
# print(os.path.join("E:","Projelerim","FileOpProject","FileOperations","file.csv"))
"""
Açma Modları
r = read mode - Varsayılan Mod
w = write mode - Dosya yoksa oluşturur, varsa içeriğini siler
a = append mode - Dosya yoksa oluşturur, varsa sonuna ekler
x = create mode - Dosya yoksa oluşturur, varsa hata verir
x+,w+,a+,r+ = read and write mode
rb,wb,ab,rb+,wb+,ab+ = binary mode
"""
dosya = open(r"FileOperations\file.csv") # r modu varsayılan moddur
"""
1. read
2. readline
3. readlines
"""
# print(dosya.read()) # read fonksiyonu dosyanın tamamını okur str veri tipinde verir
# print(dosya.readline()) # readline fonksiyonu bir satır okur str veri tipinde verir
# print(dosya.readline()) 
# print(dosya.readline())
# print(dosya.readlines()) # readlines fonksiyonu dosyayı okur ve liste veri tipinde verir