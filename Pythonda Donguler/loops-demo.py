'''
# 1 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
    **random modülü için python random şeklinde arama yapın
    **100 üzerinden puanlama yapın, her soru 20 puan.
    **Hak bilgisini kullanıcıdan alın ve her sou belirtilen can sayısı üzerinden hesaplansın.

'''

import random

sayi=random.randint(1,10)
can= int(input('Kaç hak kullanmak istersiniz:'))
hak= can
sayac=0
p=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin = int(input('Sayı Tahmininiz:'))
    if tahmin==sayi and p<=100:
         p=100-((100/can)*sayac)
         print(f'Tebikler {sayac}.defada bildiniz + {p} kazandınız')
         break
    elif tahmin < sayi :
        print('daha büyük olmalı')
    else:
        print('daha küçük olmalı')

    if hak==0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')
print(p)

