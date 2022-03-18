class cokgen:
    geometri = "Cokgenler"
    def __init__(self,kenarsayisi,cokgeninadi,acilistesi):   # contructor Yapıcı Fonksiyon
        self.kenarsayisi = kenarsayisi
        self.cokgeninadi = cokgeninadi
        self.acilistesi = acilistesi
        
    def cokgenAdiSoyle(self):
        print("Cokgenin Adı",self.cokgeninadi)
        print("Kenar Sayisi",self.kenarsayisi)


    @classmethod
    def cokgenGetir(cls):
        print(cls.geometri)

    def __del__(self): # desctructor  # nesne silindiğinde ya da program çalışmayı durdurduğunda çalışır
        print("R.I.P =>",self.adi)

ucgen = cokgen("3","dikucgen","ikizkenarucgen")
kare = cokgen("4","dörtgen",)

cokgenAdiSoyle()
ucgen.kenarsayisi()
kare.kenarsayisi()

ucgen.cokgenGetir()
kare.cokgenGetir()