import time
import random
from Hero import Hero
class TurkishHero(Hero):
    def __init__(self,name,power,health):
        self.name = name
        self.power = power
        self.health = health

    def vur(self):
        return random.randint(self.power//2, self.power)

    def darbe(self,power):
        self.health -= power

    def durum(self):
        print(self.name,":",self.health)

    def __del__(self):
        print("R.I.P",self.name)


class MalkocOglu(TurkishHero):
    def __init__(self):
        super().__init__("MalkocOglu", 300, 1150)



class BattalGazi(TurkishHero):
    def __init__(self):
        super().__init__("Battal Gazi", 350, 1200)



class Tarkan(TurkishHero):
    def __init__(self):
        super().__init__("Tarkan", 325, 1250)