luku = 3
while luku <= 1000:
    print(luku)
    luku = luku + 3

tuumat = float(input('Anna tuumamäärä: '))
while tuumat >= 0:
    sentit = tuumat * 2.54
    print('Senttimetreinä:', sentit, 'cm')
    tuumat = float(input('Anna tuumamäärä: '))

luvut = []
syote = input('Anna luku: ')
while syote != "":
    luku = float(syote)
    luvut.append(luku)
    syote = input('Anna luku: ')
    print('Pienin luku:', min(luvut))
    print('Suurin luku:', max(luvut))

import random
oikea_luku = random.randint(1, 10)
arvaus = int(input('Arvaa lukuväliltä 1-10: ')) 
while arvaus != oikea_luku:
    if arvaus > oikea_luku:
        print('Liian suuri arvaus')
    else:
        print('Liian pieni arvaus')
arvaus = int(input('Arvaa uudelleen: '))
print('Oikein!')

yritykset = 0
while yritykset < 5:
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    if tunnus == 'python' and salasana == 'rules':
        print('Tervetuloa')
        break
    else:
        yritykset = yritykset + 1
        if yritykset == 5:
            print('Pääsy evätty')

import random
N = int(input('Anna arvottavien pisteiden määrä: '))
n = 0
i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n = n + 1
        i = i +1
        pi = 4* n/N
        print('Piin likiarvo on:', pi)