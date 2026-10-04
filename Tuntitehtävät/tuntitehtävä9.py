#class rectangle:
  #  def __init__(self,length, width):
     #   self.length = length
       # self.width = width

#r1 = rectangle(23,30)
#r2 = rectangle( 45, 60)


#def walk(self):
   # print(f'{self.name} kävelee')
#p1 = Person('James', 45)
#p2 = Person('Matti', 38)

#p1.walk()
#p2.walk()


#class Rectangle:
   # def __init__(self, width, height):
      #  self.width = width
      #  self.height = height
   # def piiri(self):
       # piiri = self.height *2 + self.width
       # return piiri

#r1 = Rectangle(3,4)
#r2 = Rectangle(5,10)
#print(r1.piiri())


#class Person:
 #   def __init__(self, name, age):
  #      self.name = name
  #      self.age = age
   # def is_adult(self):
      #  if self.age >= 18:
      #      print(f'{self.name} on aikuinen')
     #   else:
        #    print('ei ole aikuinen')

#p1.is_adult()

#class Book:
 #   def __init__(self, kirjailija, kirjan_nimi, sivumäärä = 100):
      #  self.kirjailija = kirjailija
     #   self.kirjan_nimi = kirjan_nimi
     #   self.sivumäärä = sivumäärä
#b1 = Book ('Kia','Tiivitaavi', 45)
#b2 = Book ('Pekka', 'Autot', 50)
#b3 = Book ('Leena', 'Kissat', 35)
#b4 = Book ('Keijo', 'Koirat')
#print(b4.sivumäärä)

#class Ope:
    #def __init__(self, nimi):
        #self.nimi = nimi
    #def mun_stu(self, opis):
      #  print(f'Minä olen {self.nimi} Mun opiskelijan nimi on {opis.nimi}')
        

#class Opiskelija:
  #  def __init__(self, nimi):
 #       self.nimi = nimi
#op1 = Ope ('Ope1')
#opis1 = Opiskelija ('Opiskelija1')
#op1.mun_stu(op1, opis1)



#class Kirjailija:
  #  def __init__(self, nimi):
 #       self.nimi = nimi
#k1 = Kirjailija ('kirjailija1')
#k2 = Kirjailija ('kirjailija2')


                 
#class Kirja:
   # def __init__(self, nimi, kirjailija):
    #    self.nimi = nimi
    #    self.kirjailija = kirjailija
#kir1 = Kirja ('kissa', k1)
#kir2 = Kirja ('koira', k2)
#print(f'Kirjan nimi on {k1.nimi} ja sen kirjailija on {kir1.kirjailija.nimi}')

#class Asukas:
 #   def __init__(self, nimi):
    #    self.nimi = nimi
#asukas1 = ('Eemeli')
#asukas2= ('Tuomas')

#class Kaupunki:
    #def __init__(self, nimi, asukas):
      #  self.nimi = nimi
      #  self.asukas = asukas
    #def kuka (self):
 #           print(f'{self.asukas1.nimi} asuu {kaupunki1.nimi}')
#kaupunki1 = ('Helsinki',asukas1)
#kaupunki2 = ('Rovaniemi', asukas2)

#class Tili:
 #   def __init__(self, saldo):
 #       self.saldo = 100
#    def talletus(self,määrä):
   #     self.saldo = self.saldo + määrä
   #     print(f'Tässä saldo {self.saldo}')
   # def nosto(self, määrä):
     #   self.saldo = self.saldo - määrä
      #  print(f'Tässä saldo = {self.saldo}')
#t1.talletus(50)
#t1.nosto(100)
#print(t1.saldo)

class Kirja:
    def __init__(self,nimi):
        self.nimi = nimi

class Kirjasto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kirjat = []
    def lisaa_kirja(self, kirja):
        self.kirjat.append(kirja)

k1 = Kirja('Maila')
k2 = Kirja('Tuntematon Sotilas')
k3 = Kirja('Aakkoset')
k4 = Kirja('Raamattu')

kir1 = Kirjasto ('Oodi')
kir1.lisaa(k1)
kir1.lisaa(k2)
kir1.lisaa(k3)
for item in kir1.kirjat:
    print(item.nimi)