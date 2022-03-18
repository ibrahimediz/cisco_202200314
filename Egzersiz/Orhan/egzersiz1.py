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
     