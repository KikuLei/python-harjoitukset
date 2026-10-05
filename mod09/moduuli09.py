import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    
    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        
    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tuntimaara

#TEHTÄVÄ 1
auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)

print("Huippunopeus:", auto.huippunopeus)

print("Nopeus:", auto.nopeus)

print("Kuljettu matka:", auto.kuljettu_matka)

#TEHTÄVÄ 2
auto.kiihdyta(30)

auto.kiihdyta(70)

auto.kiihdyta(50)

print("Nopeus:", auto.nopeus)

auto.kiihdyta(-200)

print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus)

#TEHTÄVÄ 3
auto = Auto("ABC-123", 142)

auto.nopeus = 60

auto.kuljettu_matka = 2000

auto.kulje(1.5)

print("Kuljettu matka:", auto.kuljettu_matka)

#TEHTÄVÄ 4
autot = []

for i in range(10):

    rekisteritunnus = "ABC-" + str(i + 1)

    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)

    autot.append(auto)

while True:

    for auto in autot:

        muutos = random.randint(-10, 15)

        auto.kiihdyta(muutos)

        auto.kulje(1)

    kilpailu_loppui = False

    for auto in autot:

        if auto.kuljettu_matka >= 10000:

            kilpailu_loppui = True

    if kilpailu_loppui:

        break

print("Kilpailun tulokset:")

for auto in autot:

    print(

        auto.rekisteritunnus,

        auto.huippunopeus,

        auto.nopeus,

        auto.kuljettu_matka

    )