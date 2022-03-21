class Personel: #eposta,dogumyili,cinsiyet,pozisyon
    personelList = []
    def __init__(self,adi,soyadi,telefon,pozisyon,erisim=""):
        self.adi = adi # instance attribute örnek özellik
        self.soyadi = soyadi
        self.telefon = telefon
        self.pozisyon = pozisyon 
        self.__id = len(Personel.personelList) + 1
        Personel.personelList.append(self.__id)


    def bilgiKarti(self):
        print("#"*30,self.adi,self.soyadi,self.telefon,"#"*30,sep="\n")

    def erisimAyarla(self,obj):
        self.erisim = obj.pozisyon

    @property
    def id(self):
        if self.erisim == "M":
            return "Personel ID:" + str(self.__id)
        else:
            raise Exception("Role Error")


pers1 = Personel("İbrahim", "EDİZ", "555222222", "M")
pers2 = Personel("Sinan","Jamiryo","5522222","P")
pers2.erisimAyarla(pers1)
print(pers2.id)