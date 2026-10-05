import random

#TEHTÄVÄ 1
class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):

        self.alin_kerros = alin_kerros

        self.ylin_kerros = ylin_kerros

        self.kerros = alin_kerros

    def kerros_ylos(self):

        if self.kerros < self.ylin_kerros:

            self.kerros = self.kerros + 1

        print("Hissi on kerroksessa:", self.kerros)

    def kerros_alas(self):

        if self.kerros > self.alin_kerros:

            self.kerros = self.kerros - 1

        print("Hissi on kerroksessa:", self.kerros)

    def siirry_kerrokseen(self, kohdekerros):

        while self.kerros < kohdekerros:

            self.kerros_ylos()

        while self.kerros > kohdekerros:

            self.kerros_alas()

hissi = Hissi(1, 7)

hissi.siirry_kerrokseen(5)

hissi.siirry_kerrokseen(1)

#TEHTÄVÄ 2
class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):

        self.alin_kerros = alin_kerros

        self.ylin_kerros = ylin_kerros

        self.hissit = []

        for i in range(hissien_maara):

            hissi = Hissi(alin_kerros, ylin_kerros)

            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):

        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)

talo.aja_hissia(2, 8)

talo.aja_hissia(3, 3)

#TEHTÄVÄ 3
class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):

        self.alin_kerros = alin_kerros

        self.ylin_kerros = ylin_kerros

        self.hissit = []

        for i in range(hissien_maara):

            hissi = Hissi(alin_kerros, ylin_kerros)

            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):

        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):

        for hissi in self.hissit:

            hissi.siirry_kerrokseen(self.alin_kerros)

talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)

talo.aja_hissia(3, 3)



#TEHTÄVÄ 4
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

class Kilpailu:

    def __init__(self, nimi, kilometrimaara, autot):

        self.nimi = nimi

        self.kilometrimaara = kilometrimaara

        self.autot = autot

    def tunti_kuluu(self):

        for auto in self.autot:

            muutos = random.randint(-10, 15)

            auto.kiihdyta(muutos)

            auto.kulje(1)

    def tulosta_tilanne(self):

        print("Kilpailun tilanne:")

        print("Rekisteri | Huippunopeus | Nopeus | Matka")

        for auto in self.autot:

            print(

                auto.rekisteritunnus,

                auto.huippunopeus,

                auto.nopeus,

                auto.kuljettu_matka
)

    def kilpailu_ohi(self):

        for auto in self.autot:

            if auto.kuljettu_matka >= self.kilometrimaara:

                return True

        return False

autot = []

for i in range(10):

    rekisteritunnus = "ABC-" + str(i + 1)

    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)

    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():

    kilpailu.tunti_kuluu()

    tunnit = tunnit + 1

    if tunnit % 10 == 0:

        kilpailu.tulosta_tilanne()

print("Kilpailu on päättynyt!")

kilpailu.tulosta_tilanne()