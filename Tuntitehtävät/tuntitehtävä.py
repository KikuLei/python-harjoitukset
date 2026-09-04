# luku1 = 2
# luku2 = 5

# print(luku2 ** luku1)
# print(luku2/luku1)

# import math
# luku1 = 100
# luku2 = 523

# print(math.log10(luku1))
# print(math.log10(luku2))
# print(f"{math.log10(luku1) : .2f}")
# print(f"{math.log10(luku2) : .2f}")


luku_tmp = input ('Anna minulle joku luku: ')
luku = int(luku_tmp)
if luku < 100:
    print('Antamasi luku oli {luku} ja Lukusi on pienempi kuin 100')

elif luku == 100:
    print('Antamasi luku oli luku ja Lukusi on sama kuin 100')
else:
    print('Antamasi luku oli luku ja Lukusi on suurempi kuin 100')




