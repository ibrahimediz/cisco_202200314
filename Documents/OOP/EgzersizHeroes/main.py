from MarvelHero import *
from DCHero import *
from TurkishHero import *
karakterList = [Deadpool,CaptainAmerica,Hulk,Superman,Batman,Wolverine,BattalGazi,MalkocOglu,Tarkan]

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