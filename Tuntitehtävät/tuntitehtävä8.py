#tup = (3, 5, 8, 10, (24, 25), 'moi', 200)

#print(len(tup))
#print(tup.index(10))
#print(10 in tup)
#for alkio in tup:
   # print(alkio)

#print(tup[::-1])

#numerot = {"Viivi": "050-1234567",
           #"Ahmed": "040-1112223",
          # "Pekka": "050-7654321"}

#for item in numerot:
    #print(f'{item}:n puhelin numero on {numerot[item]}')

#nimi = input('Anna nimi: ')
#if nimi in numerot:
    #print(f'{nimi} löytyy, numero on {numerot[nimi]}')
#else:
    #print(f'{nimi} ei löytynyt luettelosta')

#li = [2 ,3, 2, 6, 7, 3, 3]
#print(set(li))

#hedelmät = {'Appelsiini', 'Omena', 'Vesimeloni'}
#print('Omena' in hedelmät)

students = [
    {'name': 'Ella', 'age': 14, 'grade': '9'},
    {'name': 'Leo', 'age': 15, 'grade': '8'},
    {'name' : 'Aino', 'age': 14, 'grade': '10'}
]

for student in students:
    print(f'{student['name']} arvosana on {student['grade']}')

print(students[2]['name'])
print(students[2]['grade'])