class Polygon:
    familya = "Çokgen"
    def __init__(self,name,surname,phone,position,access):   # contructor Yapıcı Fonksiyon
        self.name = name
        self.surname = surname
        self.phone = phone
        self.position = position
        self.__id = len(Personal.personalList) + 1
        Personal.personalList.append(self.__id)
        

    def İnfoChart(self):
        print("#"*30,self.name,self.surname,self.phone,"#"*30,sep="\n")

    def setAccess(self,obj):
        self.access= obj.position

    @property
    def id(self):
        if self.erisim == "M":
            return "Personal ID"




poly1 = triangle(adi="Üçgen",edge="üç",angle=[45,45,90])
poly2 = square("Kare","dört",[90,90,90,90])
poly1.adiNe()
poly2.adiNe()

poly1.Kenarlar()
poly2.Kenarlar()


