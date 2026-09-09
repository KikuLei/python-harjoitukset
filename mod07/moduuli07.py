import random
def heita_noppaa(tahkot):
    luku = random.randint(1,tahkot)
    return luku
tahkot = int(input('Anna nopan tahkojen määrä: '))
luku = heita_noppaa(tahkot)
while luku != tahkot:
    print(luku)
    luku = heita_noppaa(tahkot)
    print(luku)

def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat
gallonat = float(input('Anna gallonamäärä: '))
while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print(f'{litrat} litraa')
    gallonat = float(input('Anna gallonamäärä: '))

def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa = summa + luku
    return summa
luvut = [2, 5, 3, 8]
vastaus = laske_summa(luvut)
print(vastaus)

def poista_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista
luvut= [1, 2, 3, 4, 5, 6,]
karsittu_lista = poista_parittomat(luvut)
print(luvut)
print(karsittu_lista)

import math
def yksikkohinta(halkaisija, hinta):
    sade = halkaisija/2
    sade_metreina = sade/100
    pinta_ala = math.pi*sade_metreina*2
    return hinta/pinta_ala
halkaisija1 = float(input('Anna ensimmäisen pizzan halkaisijan cm: '))
hinta1 = float(input('Anna ensimmäisen pizzan hinta: '))
halkaisija2 = float(input('Anna toisen pizzan halkaisija cm: '))
hinta2 = float(input('Anna toisen pizzan huinta: '))
yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)
if yksikkohinta1 < yksikkohinta2:
    print('Ensimmäinen pizza antaa paremman vastineen rahalle')
else:
   print('Toinen pizza antaa paremman vastineen rahalle.') 
