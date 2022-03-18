liste = ["Ahmet","Dilber","Erdal","Fatma","Filiz","Yahya","Huseyin","Ismail","Nida","Orhan","Rabia","Sevgi","Yakup"]

folder="Notlar"
filename = "oop1"
import os 
for item in liste:
    if not os.path.exists(f"{folder}"):
        os.mkdir(folder)
    if not os.path.exists(f"{folder}/{item}"):
        os.mkdir(f"{folder}/{item}")
    open(f"{folder}/{item}/oop1.py","a+")