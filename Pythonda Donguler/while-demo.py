#sayilar=[1,3,5,7,9,12,19,21]
#1-Sayılar listesini while ile ekrana yazdırın.
"""i=0
while (i<len(sayilar)):
     print(sayilar[i])
     i+=1"""

#2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
"""start= int(input('başlangıç değeri:'))
stop= int(input('bitiş değeri:'))
i=start
while i<stop :
    if  i%2==1:
        print(i)
    i+=1"""
#3-1-100 arasındaki sayıları azalan şekilde ekrana yazdırın
"""i=101
while i>0:
    i-=1
    print(i)"""

#4-Kulanıcıdan alacağınız beş sayıyı ekranda sıralı bir şekilde yazdırın.
"""sayilar= []
i=0

while i<5:
    sayi= int(input('sayı gir:'))
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print(sayilar)"""

#5-Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi altında saklayın
    #ürün sayısını kullanıcıya sorun
    #dictionary yapısında olsun
    #ürün ekleme işlemi bittiğinde ürünleri while ile ekrana yazdırın.

urunler=[]

us= int(input('Kaç ürün girişi yapacaksınız?: '))
i=0
while us>i:
     urun= input('Ürün adı:')
     fiyat=input('Ürün fiyatı:')
     urunler.append({
         'name':urun,
         'price':fiyat
     })
     i+=1
print(urunler)
