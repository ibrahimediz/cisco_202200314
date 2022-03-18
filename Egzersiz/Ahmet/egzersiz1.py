class Polygon:
    familya = "Çokgen"
    def __init__(self,name,edge,angle):   # contructor Yapıcı Fonksiyon
        self.name = name
        self.edge = edge
        self.angle = angle
        

    def adiNe(self):
        print("Çokgeninin Adı",self.name)

    def kenar(self):
        print(self.edge,"Kenarlar")

    @classmethod
    def familyaGetir(cls):
        print(cls.familya)


    def __del__(self): # desctructor  # nesne silindiğinde ya da program çalışmayı durdurduğunda çalışır
        print("Silinen Çokgen =>",self.adi)

poly1 = triangle(adi="Üçgen",edge="üç",angle=[45,45,90])
poly2 = square("Kare","dört",["]90,90,90,90")
poly1.adiNe()
poly2.adiNe()

poly1.Kenarlar()
poly2.Kenarlar()


