import time
import random
from AbstractionSample import Hero
class MarvelHero(Hero):
    def __init__(self,name,power,health):
        self.name = name
        self.power = power
        self.health = health

    def vur1(self):
        return self.power//2

    def vur2(self):
        return self.power//3

    def vur3(self):
        return self.power//4

    def vur(self):
        vurList = [self.vur1,self.vur2,self.vur3]
        return random.choice(vurList)()


    def darbe1(self,power):
        self.health -= power//2

    def darbe2(self,power):
        self.health -= power//3
    
    def darbe3(self,power):
        self.health -= power//4

    def darbe(self,power):
        darbeList = [self.darbe1,self.darbe2,self.darbe3]
        random.choice(darbeList)(power)

    def durum(self):
        print(self.name,":",self.health)

    def __del__(self):
        print("R.I.P",self.name)
    

class Deadpool(MarvelHero):
    def __init__(self):
        super().__init__("Deadpool", 250, 1500)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("Captain America", 200, 1300)

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",250,1700)


karakterList = [Deadpool,CaptainAmerica,Hulk]
P1 = random.choice(karakterList)()
P2 = random.choice(karakterList)()
while P1.health > 0 and P2.health > 0:
    time.sleep(0.5)
    P1.darbe(P2.vur())
    P2.darbe(P1.vur())
    P1.durum()
    P2.durum()
else:
    if P1.health > P2.health:
        print(P1.name,"kazandı")
    elif P1.health == P2.health:
        print("Beraber")
    else:
        print(P2.name,"kazandı")