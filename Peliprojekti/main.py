from luokat import Esine, Huone, Pelaaja



#Pelin aloitusteksti ja ohjeet tekstitiedostoista
intro = open('Peliprojekti/intro.txt', 'r', encoding='utf-8')
print(intro.read())
intro.close()

ohjeet = open('Peliprojekti/ohjeet.txt', 'r', encoding='utf-8')
print(ohjeet.read())
ohjeet.close()




#Luodaan pelissä käytettävät esineet
akku = Esine('Energia-akku', 2.5)
avainkortti = Esine('Avainkortti', 0.2)
happisailio = Esine('Happisäiliö', 3.0)


#Luodaan pelin eri paikat
komentokeskus = Huone('komentokeskus', avainkortti)
planeetta = Huone('Tuntematon planeetta', akku)
hylatty_asema = Huone('Hylätty avaruusasema', happisailio)



nimi = input('Anna pelaajan nimi: ')
ikä = int(input('Anna pelaajanikä: '))

print('Pelaajan nimi:', nimi)
print('Pelaajan ikä:', ikä)

if ikä < 12:
    print('Olet liian nuori käyttämään peliä.')
    exit()
else:
    print("Tervetuloa", nimi + "!")  
    pelaaja = Pelaaja(nimi, komentokeskus)



# Pelaaja valitsee paikan johon haluaa lentää
def lenna():
    print('Minne haluat lentää?')
    print('1. Tuntematon planeetta')
    print('2. Hylätty avaruusasema')
    print('3. Komentokeskus')
    valinta = input('Valitse kohde: ')
    if valinta == '1':
        pelaaja.liiku(planeetta)
    elif valinta == '2':
        pelaaja.liiku(hylatty_asema)
    elif valinta == '3':
         pelaaja.liiku(komentokeskus)
    else:
         print('Tuntematon kohde.')


#Tutkitaan pelaajan nykyistä paikkaa ja kerätään siellä oleva esine
def tutki_planeettaa():
     print('Tutkit paikkaa:', pelaaja.sijainti.nimi)
     pelaaja.keraa_esine()


#Näyttää pelaajan keräämät esineet
def nauta_inventaario():
    print('Inventaario: ')
    if len(pelaaja.esineet) == 0:
         print('Inventaario on tyhjä.')
    else:
         for esine in pelaaja.esineet:
              print(esine.nimi)

#Tarkistaa löytyykö tietty esine pelaajan inventaariosta
#Funkito saa parametrina esineen nimen. for käy inventaarion esineen läpi. Jos oikea esine löytyy palautetaan True, Jos ei löydy palautetaan False.
def tarkista_esine(esineen_nimi):
     for esine in pelaaja.esineet:
          if esine.nimi == esineen_nimi:
               return True
     return False


#Yritetään korjata alus tarvittavien esineiden avulla
#and tarkoittaa kaikkien kolmen ehdon täytyy olla True. return True -> pelaaja voitti -> pääsilmukka break -> peli loppuu
#Fuktiot
def korjaa_alus():
     if (tarkista_esine('Energia-akku')
         and tarkista_esine('Happisäiliö')
         and tarkista_esine('Avainkortti')):
          print('Kaikki tarvittavat esineet löytyivät!')
          print('Korjasit avaruusaluksen.')
          print('Hyödynsit vanhat osat uudelleen ja vähensit avaruusromua.')
          print('Lensit turvallisesti takaisin Maahan!')
          print('Voitit pelin!')
          return True
     else:
          print('Et voi vielä korjata alusta.')
          print('Tarvitset Energia-akun, Happisäiliön ja Avainkortin')
          return False


#Kolmas loppu: Avaruusoliot auttavat pelaajaa
#Pelaajan pitää olla planeetalla ja pitää olla happisäiliö.
def tutki_signaalia():
     if pelaaja.sijainti == planeetta and tarkista_esine('Happisäiliö'):
          print('Seuraat planeetalta kuuluvaa salaperäistä signaalia.')
          print('Signaali johdattaa sinut avaruusolioiden luokse!')
          print('Avaruusoliot auttavat sinua ja vievät sinut aluksellaan takaisin Maahan.')
          print('Voitit pelin!')
          return True
     else:
          print('Et voi seurata signaalia.')
          print('Sinun pitää olla Tuntemattomalla planeetalla ja tarvitset Happisäiliön.')
          return False


#Tankkaa avaruusalus
def tankkaa_alus():
    print('Avaruusalus tankkautuu')

#Tallentaa pelaajan nimen, sijainnin ja esineen tiedostoon
def tallenna_peli():
     tiedosto = open('save.txt', 'w')
     tiedosto.write(pelaaja.nimi + '\n')
     tiedosto.write(pelaaja.sijainti.nimi + '\n')
     for esine in pelaaja.esineet:
          tiedosto.write(esine.nimi + '\n')
     tiedosto.close()
     print('Peli tallennettu.')


#Toinen loppu: Pelaaja lähettää hätäsignaalin komentokeskuksesta.
def laheta_signaali():
     if pelaaja.sijainti == komentokeskus and tarkista_esine('Avainkortti'):
          print('Käytit Avainkorttia hätälähettimen avaamiseen.')
          print('Lähetit hätäsignaalin Maahan.')
          print('Pelastusalus saapui hakemaan sinut!')
          print('Voitit pelin!')
          return True
     else:
          print('Et voi lähettää hätäsignaalia.')
          print('Sinun pitää olla Komentokeskuksessa ja tarvitset Avainkortin.')
          return False



#Ladataan aikaisemmin tallennettu peli
def lataa_peli():
     tiedosto = open('save.txt', 'r')
     nimi = tiedosto.readline().strip()
     sijainti = tiedosto.readline().strip()
     pelaaja.esineet = []
     if sijainti == 'komentokeskus':
          pelaaja.sijainti = komentokeskus
     elif sijainti == 'Tuntematon planeetta':
          pelaaja.sijainti = planeetta
     elif sijainti == 'Hylätty avaruusasema':
          pelaaja.sijainti = hylatty_asema
     for rivi in tiedosto:
          esineen_nimi = rivi.strip()
          if esineen_nimi == 'Energia-akku':
               pelaaja.esineet.append(akku)
               planeetta.esine = ''
          elif esineen_nimi == 'Avainkortti':
               pelaaja.esineet.append(avainkortti)
               komentokeskus.esine = ''
          elif esineen_nimi == 'Happisäiliö':
               pelaaja.esineet.append(happisailio)
               hylatty_asema.esine = ''
     pelaaja.nimi = nimi
     tiedosto.close()
     print('Tallennettu pelaaja:', nimi)
     print('Tallennettu sijainti:', sijainti)
   
print('1. Uusi peli')
print('2. Lataa peli')
aloitus = input('Valitse: ')
if aloitus == '1':
     print('Aloitetaan uusi peli!')
elif aloitus == '2':
     lataa_peli()
else:
     print('Tuntematon valinta.')



#Pelin pääsilmukka, joka toimii kunnes pelaaja voittaa tai lopettaa pelin.
komento = ""
while komento != 'lopeta':
    print('PÄÄVALIKKO')
    print('lennä')
    print('korjaa')
    print('tutki')
    print('tankkaa')
    print('signaali')
    print('mysteeri')
    print('inventaario')
    print('tallenna')
    print('lopeta')
    komento = input('Anna komento: ')

#valitsee mikä funktio suoritetaan käyttäjän kirjoittaman komennon perusteella.
    if komento == 'lennä':
            lenna()
    elif komento == 'korjaa':
          if korjaa_alus() == True:
               break
    elif komento == 'tutki':
            tutki_planeettaa()
    elif komento == 'tankkaa':
          tankkaa_alus()
    elif komento == 'signaali':
         if laheta_signaali() == True:
              break
    elif komento == 'mysteeri':
         if tutki_signaalia():
              break
    elif komento == 'inventaario':
            nauta_inventaario()
    elif komento == 'tallenna':
         tallenna_peli()
         
    elif komento == 'lopeta':
            print('Avaruusseikkailu päättyy!')

