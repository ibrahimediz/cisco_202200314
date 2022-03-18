print("Merhaba")
""" Çokgenler için bir sınıf tasarlayınız 
sınıf içerisinde 3 adet instance attribute olsun kenar sayısı ve açı listesi
"""
class Cokgen:
    def __init__(self,kenarSayisi,cokgenAdi,aciListesi):
        self.kenarSayisi = kenarSayisi
        self.cokgenAdi = cokgenAdi
        self.aciListesi = aciListesi

    def cokgenadi(self):
        print("çokgenin Adı",self.cokgenAdi)

    def kenarSayisi(self):
        print("kenar sayısı",self.kenarSayisi)

    def aciListesi(self):
        print("açı listesi",self.aciListesi)



cokgen1 = Cokgen("Üçgen","üç","45,45,90")
cokgen2 = Cokgen("Kare","dört","90,90,90,90")
cokgen1.cokgenAdi()
cokgen2.cokgenadi()

