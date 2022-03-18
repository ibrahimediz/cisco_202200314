class ucgen:
   
    def __init__(self,kenarsayisi,cokgenadi,acilistesi):   # contructor Yapıcı Fonksiyon
        self.kenarsayisi = kenarsayisi
        self.cokgenadi = cokgenadi
        self.acilistesi = acilistesi
        
    def cokNe(self):
        print("cokgenAdiSoyle",self.cokgenadi)  

    def kenarNe(self):
        print("kenarsayisi",self.kenarsayisi)  

    ucgen.kenarNe(self.kenarsayisi)


class Cokgen:
    def __init__(self,kenarsayisi,cokgenadi,acilistesi):
        self.kenarsayisi = kenarsayisi
        self.cokgenadi = cokgenadi
        self.acilistesi = acilistesi

    def cokgenAdiSoyle(self):
        print(f"{self.cokgenadi} adındaki çokgenin kenar sayısı => {self.kenarsayisi} kadardır")
    

ucgen = Cokgen(3, "Üçgen", [30,60,90])
kare = Cokgen(4,"Kare",[90,90,90,90])
ucgen.cokgenAdiSoyle()
kare.cokgenAdiSoyle()
     