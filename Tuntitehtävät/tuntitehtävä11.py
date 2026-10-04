

class Biisi:
    def __init__(self,nimi, laulaja):
        self.nimi = nimi
        self.laulaja = laulaja


l1 = Biisi ('Laulu1', 'Laulaja1')
l2 = Biisi('Laulu2', 'Laulaja2')
l3 = Biisi('Laulu3', 'Laulaja3')
l4 = Biisi('Laulu4', 'Laulaja4')
l5 = Biisi ('Laulu5', 'Laulaja5')
l6 = Biisi('Laulu6', 'Laulaja6')

class Playlist:
    def __init__(self):
        self.munlista = []
    def lisaa(self, uusi):
        self.munlista.append(uusi)

pl = Playlist()
pl.lisaa(l1)
pl.lisaa(l2)
print(pl.munlista)


list =  [l1, l5, l6]
for item in list:
    print(item.laulaja)