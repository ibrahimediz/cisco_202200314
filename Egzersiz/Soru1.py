"""Çokgen bilgileri için bir sınıf oluşturalım
1. Sınıfta üç adet instance attribute olsun bunlar (kenarsayisi,cokgenadi ve acilistesi)
2. Sınıf içinde cokgenAdiSoyle adında bir fonksiyon çokgenin adını ve kenar sayısını ekrana yazdırsın
3. Üçgen ve kare için oluşturduğumuz sınıf üzerinden instance üretelim.
"""

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