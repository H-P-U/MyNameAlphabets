names=['Ali','Yağmur', 'Hakan', 'Deniz']
years=[1998, 2000, 1998, 1987]

#1-"Cenk" ismini listenin en sonuna ekleyin
'''names.append('Cenk')
print(names)'''

#2-"Sena" değerini listenin en başına ekleyin
'''names.insert(0,'Sena')
print(names)'''

#3-"Deniz" ismini listeden silin
'''names.pop(3)
print(names)'''

#4-"Deniz" isminin indeksi nedir?
'''sayi=names.index('Deniz')
print(sayi)'''

#5-"Ali" listenin bir elemanı mıdır?
'''varmi=names.index('Ali')
print(varmi)'''
'''result= 'Ali' in names
print(result)'''

#6-Liste elemanlarını ters çevirin.
'''names.reverse()
print(names)'''

#7-Liste elemanlarını alfabetik olarak sıralayın.
'''new= names.sort()
print(names)'''

#8-years listesini rakamsal büyüklüğe göre sıralayınız.
'''years.sort()
print(years)'''

#9-str= "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
'''str= "Chevrolet, Dacia"
sonuc=str.split(',')
print(sonuc)'''

#10-years dizisinin en büyük ve en küçük değeri nedir?
'''EB= max(years)
EK= min(years)
print('En büyük değer '+str(EB) + ' En küçük değer '+ str(EK))'''

#11-years dizisinde kaç tane 1998 vardır?
'''sayi=years.count(1998)
print(sayi)'''

#12-years dizisinin tüm elemanlarını silin.
'''years.clear()
print(years)'''

#13-Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayın.

markalar=[]

marka1= input('Marka1: ')
markalar.append(marka1)
marka2= input('Marka2: ')
markalar.append(marka2)
marka3=input('Marka3: ')
markalar.append(marka3)

print(markalar)
