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

ucgen=cokgen(3,üçgen, [30,60,90])


    