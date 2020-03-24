#1-Gönderilen bir parametriyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""def yazdir(kelime, adet):
    print(kelime*adet)

yazdir('Elma ',7)"""

#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

"""def ListeyeCevir(*params):
    liste=[]

    for param in params:
        liste.append(param)
    return liste

result=ListeyeCevir(1,2,3,4,'selam')

print(result)"""

#3-Gönderilen iki sayı arasındaki tüm asal sayıları bulun.

"""
def AsalSayilariBul(value1, value2):
    for num in range(value1, value2):
        if num>1:
            for i in range(2, num):
                if (num%i==0):
                    break
            else:
                print(num)

value1= int(input('Sayı 1:'))
value2= int(input('Sayi 2:'))
AsalSayilariBul(value1, value2)
"""
#4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazın.

def TamBolenleriListele(sayi):
    TamBolenler=[]

    for k in range(2, sayi):
        if (sayi%k==0 ):
             TamBolenler.append(k)
    return TamBolenler

sayi= int(input('Sayı Gir:'))
print(TamBolenleriListele(sayi))
