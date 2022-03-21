import time
class MarvelHero:
    def __init__(self,name,power,health):
        self.name = name
        self.power = power
        self.health = health

    def vur(self):
        return self.power

    def darbe(self,power):
        # self.health = self.health - self.guc
        self.health -= power

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

        





karakterList = [Deadpool,CaptainAmerica]
P1 = karakterList[0]()
P2 = karakterList[1]()
while P1.health > 0 and P2.health > 0:
    time.sleep(1)
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