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