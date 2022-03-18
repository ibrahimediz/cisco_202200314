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

kayitlar = []
adres = r"FileOperations\rehber.csv"
dosya1 = open_file(adres)
kayitlar =  dosya1.readlines()
alanlar = ["Ad","Soyad","Telefon"]

def kayitListele():
    for _id,kayit in enumerate(kayitlar):
        print(f"{_id}",*kayit.split(";"),end="",sep="-")

def girisAl():
    liste = []
    for item in alanlar:
        liste.append(input(f"{item}: "))
    return ";".join(liste) + "\n"


def kayitguncelle():
    kayitListele()
    kayitlar[int(input("Güncellenecek kayıt numarası: "))] = girisAl()

def kayitekle():
    kayitlar.append(girisAl())

def kayitsil():
    kayitListele()
    _id = int(input("Silinecek kayıt numarası: "))
    del kayitlar[_id]

def menu():
    menuMetin = f"""
    {adres} adresindeki dosya üzerinde işlem yapılıyor
    1.Ekle
    2.Güncelle
    3.Sil
    4.Listele
    5.Çıkış
    """
    fonkList = [kayitekle,kayitguncelle,kayitsil,kayitListele]
    anahtar  = 0
    while anahtar == 0:
        islem = input(menuMetin)
        if islem and islem.isdigit():
            if int(islem) in range(5):
                fonkList[int(islem)-1]()
            elif int(islem) == 5:
                anahtar = 1
            else:
                print("Geçersiz işlem")
        else:
            print("Geçersiz işlem")
    else:
        dosya1.seek(0) # dosya1.seek(0) imleci dosya başına alır
        dosya1.truncate() # dosya1.truncate() dosyayı sıfırlar
        dosya1.writelines(kayitlar) # dosya1.writelines(kayitlar) dosyaya kayitlar listesini yazar
        dosya1.close() # dosya1.close() dosyayı kapatır




menu()