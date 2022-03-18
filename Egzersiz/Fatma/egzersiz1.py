class cokgen:
    
    def __init__(kenarsayisi,cokgenadi,aciliste):   # contructor Yapıcı Fonksiyon
        self.kenarsayisi = kenarsayisi
        self.cokgenadi = cokgenadi
        self.aciliste = aciliste
        #self.yas = 1 

    def cokgenadiSoyle(self):
        print("cokgenadi",self.cokgenadi)

    def kenarSayisi(self):
        print(self.kenarsayisi,"kenarsayisi")

    @classmethod
    def familyaGetir(cls):
        print(cls.familya)


    def __del__(self): # desctructor  # nesne silindiğinde ya da program çalışmayı durdurduğunda çalışır
        print("R.I.P =>",self.adi)

kedi1 = Kedi(adi="Melek",goz="Yeşil",tuy="Kısa",cins="Tekir")
kedi2 = Kedi("Miskin","Mavi","Uzun","Scottish")
kedi1.adiNe()
kedi2.adiNe()

kedi1.beslenme()
kedi2.beslenme()

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