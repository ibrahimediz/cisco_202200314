class Cokgen:
    def __init__(self,kenarsayisi,cokgenadi,acilistesi):  
        self.cokgenadi = cokgenadi
        self.acilistesi= acilistesi
        
    def cokgenAdiSoyle(self):
        print("Çokgenin Adı",self.cokgenadi)
        print(self.kenarsayisi,"Kenar sayısı")

ucgen = cokgen("3","dikucgen","ikizkenarucgen")
kare = cokgen("4","dörtgen",)

ucgen.cokgenAdiSoyle()
ucgen.cokgenAdiSoyle()
ucgen.kenarsayisi()
kare.kenarsayisi()

