liste = ["Ahmet","Dilber","Erdal","Fatma","Filiz","Yahya","Huseyin","Ismail","Nida","Orhan","Rabia","Sevgi","Yakup","AliImran"]

folder="Notlar"
filename = "InheritanceSample1.py"
import os 
for item in liste:
    if not os.path.exists(f"{folder}"):
        os.mkdir(folder)
    if not os.path.exists(f"{folder}/{item}"):
        os.mkdir(f"{folder}/{item}")
    if not os.path.exists(f"{folder}/{item}/{filename}.py"):
        open(f"{folder}/{item}/{filename}.py","w+")