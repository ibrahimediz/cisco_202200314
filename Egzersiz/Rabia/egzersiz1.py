class cokgen:
    geometri = "Cokgenler"
    def __init__(self,kenarsayisi,cokgeninadi,acilistesi):   # contructor Yapıcı Fonksiyon
        self.kenarsayisi = kenarsayisi
        self.cokgeninadi = cokgeninadi
        self.acilistesi = acilistesi
        
    def cokgenAdiSoyle(self):
        print("Cokgenin Adı",self.cokgeninadi)
        print("Kenar Sayisi",self.kenarsayisi)


ucgen = cokgen("3","dikucgen","ikizkenarucgen")
kare = cokgen("4","dörtgen",)

ucgen.cokgenAdiSoyle()
ucgen.cokgenAdiSoyle()
ucgen.kenarsayisi()
kare.kenarsayisi()
