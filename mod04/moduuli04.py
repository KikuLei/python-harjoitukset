pituus = float(input('Anna kuhan pituus senttimetreinä: '))
if pituus < 37:
    puuttuu = 37 - pituus
    print('Kuha on alamittainen.')
    print('Laske kuha takaisin järveen.')
    print('Sallitusta pituudesta puuttuu', puuttuu, "cm.")

hyttiluokka = input('Anna hyttiluokka (LUX, A, B tai C): ')
if hyttiluokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka =='A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')

sukupuoli = input('Anna biologinen sukupuoli (nainen/mies): ')
hemoglobiini = float(input('Anna hemoglobiiniarvo (g/l) '))
if sukupuoli == 'nainen':
    if hemoglobiini < 117:
        print('Hemoglobiiniarvo on alhainen.')
    elif hemoglobiini <= 175:
        print('Hemoglobiiniarvo on normaali.')
    else:
        print('Hemoglobiiniarvo on korkea.')

elif sukupuoli == 'mies':
    if hemoglobiini < 134:
        print('Hemoglobiiniarvo on alhainen.')
    elif hemoglobiini <= 195:
        print('Hemoglobiiniarvo on normaali.')
    else:
        print('Hemoglobiiniarvo on korkea.')

vuosi = int(input('Anna vuosiluku: '))
if vuosi % 400 == 0:
    print('Vuosi on karkausvuosi.')
elif vuosi % 100 == 0:
    print('Vuosi ei ole karkausvuosi.')
elif vuosi % 4 == 0:
    print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')