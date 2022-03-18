liste = ["Ahmet","Dilber","Erdal","Fatma","Filiz","Yahya","Huseyin","Ismail","Nida","Orhan","Rabia","Sevgi","Yakup"]

import os 
for item in liste:
    os.mkdir(f"Egzersiz/{item}")
    open(f"Egzersiz/{item}/oop1.py","w+")