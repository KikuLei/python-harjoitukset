#TEHTÄVÄ 1
class Julkaisu:

    def init(self, nimi):

        self.nimi = nimi

class Kirja(Julkaisu):

    def init(self, nimi, kirjoittaja, sivumaara):

        super().init(nimi)

        self.kirjoittaja = kirjoittaja

        self.sivumaara = sivumaara

    def tulosta_tiedot(self):

        print("Nimi:", self.nimi)

        print("Kirjoittaja:", self.kirjoittaja)

        print("Sivumäärä:", self.sivumaara)

class Lehti(Julkaisu):

    def init(self, nimi, paatoimittaja):

        super().init(nimi)

        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):

        print("Nimi:", self.nimi)

        print("Päätoimittaja:", self.paatoimittaja)

lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()

kirja.tulosta_tiedot()


#TEHTÄVÄ 2
class Auto:

    def init(self, rekisteritunnus, huippunopeus):

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

class Sahkoauto(Auto):

    def init(self, rekisteritunnus, huippunopeus, akkukapasiteetti):

        super().init(rekisteritunnus, huippunopeus)

        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):

    def init(self, rekisteritunnus, huippunopeus, bensatankki):

        super().init(rekisteritunnus, huippunopeus)

        self.bensatankki = bensatankki

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)

polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.nopeus = 120

polttomoottoriauto.nopeus = 100

sahkoauto.kulje(3)

polttomoottoriauto.kulje(3)

print("Sähköauton matkamittari:", sahkoauto.kuljettu_matka, "km")

print("Polttomoottoriauton matkamittari:", polttomoottoriauto.kuljettu_matka, "km")