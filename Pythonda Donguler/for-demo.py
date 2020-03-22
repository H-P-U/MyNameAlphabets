'''sayilar=[1,3,5,7,9,12,19,21]'''
#1-Sayılar listesindeki hangi sayılar 3'ün katıdır?
'''for i in sayilar:
    if i%3==0:
        print(i)'''
#2-Sayılar listesindeki sayıların toplamı kaçtır?
'''sum=0
for i in sayilar:
    sum+=i
print(sum)'''
#3-Sayılar listesindeki tek sayıların karesini alın.
'''for s in sayilar:
    sq=s**2
    print(sq)'''
sehirler=['kocaeli','istanbul','ankara','izmir','rize']
#4-Şehirlerden hangileri en fazla 5 karakterlidir?
'''for c in sehirler:
    if len(c)<=5:
        print(c)'''

urunler=[
    {'name': 'Samsung S6', 'price':'3000'},
    {'name': 'Samsung S7', 'price':'4000'},
    {'name': 'Samsung S8', 'price':'5000'},
    {'name': 'Samsung S9', 'price':'6000'},
    {'name': 'Samsung S10', 'price':'7000'}
]
#5-Ürünlerin fiyatları toplamı nedir?
'''sum=0
for u in urunler:
    sum+=int(u['price'])
print(sum)'''

#6-Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for u in urunler:
    if int(u['price'])<=5000:
        print(u)
