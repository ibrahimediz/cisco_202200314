"""Çokgen bilgileri için bir sınıf oluşturalım
1. Sınıfta üç adet instance attribute olsun bunlar (kenarsayisi,cokgenadi ve acilistesi)
2. Sınıf içinde cokgenAdiSoyle adında bir fonksiyon çokgenin adını ve kenar sayısını ekrana yazdırsın
3. Üçgen ve kare için oluşturduğumuz sınıf üzerinden instance üretelim.
"""
class Cokgenler:
    Sekil = "Cokgenler"
    def __init__(self,kenarsayisi,kosesayisi,sekiladi,icacisi):   # contructor Yapıcı Fonksiyon
        self.kenarsayisi = kenarsayisi
        self.kosesayisi = kosesayisi
        self.sekiladi = sekiladi
        self.icacisi = icacisi
        #self.yas = 1 

    def adiNe(self):
        print("Çokgenin Adı",self.sekiladi)

    def sekiladi(self):
        print(self.kosesayisi,"Şeklin Köşe Sayısı")

    @classmethod
    def tumSekiller(cls):
        print(cls.Sekil)


    def __del__(self): # desctructor  # nesne silindiğinde ya da program çalışmayı durdurduğunda çalışır
        print("R.I.P =>",self.sekiladi)

ucgen = Üçgen(kenarsayisi="3",kosesayisi="3",sekiladi="Üçgen", icacisi="60")
kare = Kare(kenarsayisi="4",kosesayisi="4",sekiladi="Kare", icacisi="90")
besgen = Beşgen(kenarsayisi="5",kosesayisi="5",sekiladi="Beşgen", icacisi="120")
ucgen.adiNe()
kare.adiNe()
besgen.adiNe()

ucgen.kenarsayisi()
kare.kenarsayisi()

kedi1.yas +=1
print(kedi1.yas)
print(kedi2.yas)

print(Kedi.familya)
kedi1.familya = "Jamiryo" # kedi1 için bir instance attribute üretildi class attribute e erişilemez
print(kedi1.familya)
print(kedi2.familya)

Kedi.familyaGetir()
kedi1.familyaGetir()
kedi2.familyaGetir()