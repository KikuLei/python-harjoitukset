#1 
vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')
kuukausi = int(input('Anna kuukauden numero (1-12): '))
vuodenaika = vuodenajat[kuukausi % 12 //3 ]
print(f'{kuukausi}. Vuodenaika on {vuodenaika}.')

#2
nimet = set()
while True:
    nimi = input('Anna nimi: ')

    if nimi == '':
        break
    if nimi in nimet:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
        nimet.add(nimi)
print('Syötetyt nimet:')
for nimi in nimet:
    print(nimi)

#3
lentokentat = {}
while True:
    toiminto = input('Valitse: uusi, hae tai lopeta: ')
    if toiminto == 'uusi':
        icao = input('Anna lentokentän ICAO-koodi: ')
        nimi = input('Anna lentokentän nimi: ')
        lentokentat[icao] = nimi
    elif toiminto == 'hae':
        icao = input('Anna lentokentän ICAO-koodi: ')
        if icao in lentokentat:
            print(lentokentat[icao])
        else:
            print('Lentokenttää ei löytynyt.')
    elif toiminto == 'lopeta':
        break