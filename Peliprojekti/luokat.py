#Pelissä käytettävät luokat ja oliot
class Esine:
    def __init__(self, nimi, paino):
          self.nimi = nimi
          self.paino = paino
class Huone:
    def __init__(self, nimi, esine):
          self.nimi = nimi
          self.esine = esine


#kohde on patametri, joka kertoo mihin paikkaan pelaaja liikkuu
class Pelaaja:
    def __init__(self, nimi, sijainti):
          self.nimi = nimi
          self.esineet = []
          self.sijainti = sijainti
    def liiku(self, kohde):
          self.sijainti = kohde
          print(f'Siirrytään paikkaan: {kohde.nimi}')


    def keraa_esine(self):
#Jos pelaajan nykyisessä sijainnissa on esine 
          if self.sijainti.esine != '':
            esine = self.sijainti.esine
            self.esineet.append(esine)
#Poistaa esineen paikasta josta se on kerätty
            self.sijainti.esine = ''
            print('Keräsit esineen:', esine.nimi) 
          else:
            print('Täällä ei ole esinettä.')