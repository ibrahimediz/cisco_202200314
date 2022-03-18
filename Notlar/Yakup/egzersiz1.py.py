"""
class
instance
"""
"""
attribute
method
"""
######################### ilk tanım ###########################
# class Sinif: #class
#     pass 
# Sinif() # instance


# class Sinif:
#     sinifOzelligi = "Sınıf Özelliği" # class attribute
#     def __init__(self,a):
#         self.a = a # instance attribute
    
#     def ornekMethod(self): # instance method
#         return self.a 


class Cokgen:
    #familya = "Felis"
    def __init__(self,kenarsayisi,adi,acilistesi):   # contructor Yapıcı Fonksiyon
        self.kenarsayisi = kenarsayisi
        self.adi = adi
        self.acilistesi = acilistesi
        

    def cokgenKenarsayisi(self):
        print("Cokgen Kenar Sayısı",self.kenarsayisi)

    def cokgenAdi(self):
        print("cokgenAdi", self.adi)

    def aciListesi(self):
        print(("aciListesi", self.aciListesi))

ucgen = Cokgen(3, "üçgen", acilistesi)

    

# kedi1 = Kedi(adi="Melek",goz="Yeşil",tuy="Kısa",cins="Tekir")
# kedi2 = Kedi("Miskin","Mavi","Uzun","Scottish")
# kedi1.adiNe()
# kedi2.adiNe()

# kedi1.beslenme()
# kedi2.beslenme()

