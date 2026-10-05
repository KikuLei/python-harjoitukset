import random
maara = int(input('Anna arpakuutioiden lukumäärä: '))
summa = 0
for i in range(maara):
    noppa = random.randint(1, 6)
    print('Silmälukujen summa on:', summa)

luvut = []
syote = input('Anna luku: ')
while syote !='':
    luku = float(syote)
    luvut.append(luku)
    syote = input('Anna luku: ')
    luvut.sort(reverse=True)
    for luku in luvut [:5]:
        print(luku)

luku = int(input('Anna kokonaisluku: '))
alkuluku = True
if luku < 2:
    alkuluku = False
else:
    for i in range(2,luku):
        if luku % i == 0:
            alkuluku = False
if alkuluku:
    print('Luku on alkuluku.')
else:
    print('Luku ei ole alkuluku.')

kaupungit = []
for i in range (5):
    kaupunki = input('Anna kaupungin nimi: ')
    kaupungit.append(kaupunki)
    print('Kaupungit: ')
    for kaupunki in kaupungit:
        print(kaupunki)
