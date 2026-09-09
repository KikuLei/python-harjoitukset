nimi = input('Anna pelaajan nimi: ')
ikä = int(input('Anna pelaajanikä: '))

print('Pelaajan nimi:', nimi)
print('Pelaajan ikä:', ikä)

if ikä < 12:
    print('Olet liian nuori käyttämään peliä.')
else:
    print("Tervetuloa", nimi + "!")
    komento = ""
    while komento != 'lopeta':
        print()
        print('PÄÄVALIKKO')
        print('lennä')
        print('tutki')
        print('tankkaa')
        print('lopeta')
        komento = input('Anna komento: ')
        if komento == 'lennä':
            print('Avaruusalus lähtee kohti uutta planeettaa!')
        elif komento == 'tutki':
            print('Tutkit tuntematonta planeettaa ja löydät hylätyn avaruusaluksen')
        elif komento == 'tankkaa':
            print('Avaruusalus tankattu!')
        elif komento == 'lopeta':
            print('Avaruusseikkailu päättyy!')

inventaario = []
def tutki_planeettaa():
    esine = input('Löysit jotain planeetalta. Mikä esine löytyi?')
    inventaario.append(esine)
    print(f'{esine} lisättiin inventaarioon.')
def nauta_inventaario():
    print('Inventaario: ')
    for esine in inventaario:
        print(esine)
def korjaa_alus():
    print('Korjaa avaruusalustasi.')
while True:
    print('\n---AVARUUSPELI.')
    print('1. Tutki planeettaa')
    print('2. Näytä inventaario')
    print('3. Korjaa avaruusalus')
    print('4. Lopeta')

    valinta = input('Valitse toiminto: ')

    if valinta == '1':
        tutki_planeettaa()
    elif valinta == '2':
        nauta_inventaario()
    elif valinta == '3':
        korjaa_alus()
    elif valinta == '4':
        print('Peli päättyi.')
        break
    else:
        print('Virheellinen valinta.')
