import time
import random
from Hero import Hero
class DCHero(Hero):
    def __init__(self,name,power,health,superguc=5):
        self.name = name
        self.power = power
        self.health = health
        self.superguc = superguc
    def vur(self):
        return random.randint(self.power//2, self.power)

    def darbe(self,power):
        self.superguc -= 1
        if not self.superguc:
            print("#"*10,self.name,"Süper Güç Kullandı",10*"#")
            self.health = 1000
        else:
            self.health -= power
        


    def durum(self):
        print(self.name,":",self.health)

    def __del__(self):
        print("R.I.P",self.name)


class Superman(DCHero):
    def __init__(self):
        super().__init__("Superman", 300, 1150)



class Batman(DCHero):
    def __init__(self):
        super().__init__("Batman", 350, 1200)



class Wolverine(DCHero):
    def __init__(self):
        super().__init__("Wolverine", 325, 1250)