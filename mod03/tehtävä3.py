#nimi = input ('Kerro nimesi: ')
#print('Terve, ',nimi + "!")

import math
sade = float(input('Anna ympyrän säde: '))
pinta_ala = math.pi *sade ** 2
print(f'Ympyrän pinta-ala on {pinta_ala: .2f}')

kanta = float(input('Anna suorakulmion kanta: '))
korkeus = float(input('Anna suorakulmion korkeus: '))

pinta_ala = kanta * korkeus
piiri = 2 * kanta + 2 * korkeus

print("Suorakulmion pinta-ala on", pinta_ala)
print('Suorakulmion piiri on', piiri)

luku1 = int(input('Anna ensimmäinen kokonaisluku: '))
luku2 = int(input('Anna toinen kokonaisluku: '))
luku3 = int(input('Anna kolmas kokonaisluku: '))

summa = luku1 + luku2 + luku3
tulo = luku1 *luku2 * luku3
keskiarvo = summa / 3

print('Lukujen summa on', summa)
print('Lukujen tulo on', tulo)
print('Lukujen keskiarvo on', keskiarvo)


leiviskät = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))
luodit_yhteensä = leiviskät * 20 * 32 + naulat * 32 + luodit
grammat = luodit_yhteensä * 13.3
kilogrammat = int(grammat // 1000)
grammat_jäljellä = grammat % 1000
print('Massa nykymittojen mukaan: ')
print(f"{kilogrammat} kilogrammaa ja {grammat_jäljellä:.2f} grammaa.")


import random

numero1 = random.randint(0, 9)
numero2 = random.randint (0, 9)
numero3 = random.randint(0, 9)

print('Kolmenumeroinen koodi:', numero1, numero2, numero3)

numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)

print('Nelinumeroinen koodi:', numero4, numero5, numero6, numero7, sep="")