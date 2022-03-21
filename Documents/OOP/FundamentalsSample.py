# class Personel: #eposta,dogumyili,cinsiyet,pozisyon
#     def __init__(self,adi,soyadi,telefon):
#         self.adi = adi # instance attribute örnek özellik
#         self.soyadi = soyadi
#         self.telefon = telefon


#     def bilgiKarti(self):
#         print("#"*30,self.adi,self.soyadi,self.telefon,"#"*30,sep="\n")

# personel1 = Personel("İbrahim", "EDİZ", "50522222222")
# personel2 = Personel("Ali","KATI","55511111111")
# personel1.bilgiKarti()
# personel2.bilgiKarti()
####################################### class attribute olarak liste eklemek ve personellere otomatik ID vermek
class Personel: #eposta,dogumyili,cinsiyet,pozisyon
    personelList = []
    def __init__(self,adi,soyadi,telefon,yetki):
        self.adi = adi # instance attribute örnek özellik
        self.soyadi = soyadi
        self.telefon = telefon
        self.yetki = yetki
        self.id = len(Personel.personelList) + 1
        Personel.personelList.append(self.id)

    def bilgiKarti(self):
        print("#"*30,self.adi,self.soyadi,self.telefon,self.id,"#"*30,sep="\n")
    
    def idSoyle(self):
        print("Kullanici ID",self.id)


personel1 = Personel("İbrahim", "EDİZ", "50522222222",1)
personel2 = Personel("Ali","KATI","55511111111",1)
personel1.bilgiKarti()
personel2.bilgiKarti()
personel1.idSoyle()
personel2.idSoyle()