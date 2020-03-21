#1-Girilen bir sayının 0-100 arasında olup olmadığını kontol edin.
'''sayi= int(input('Sayi Gir:'))
result= (0<sayi) and (sayi<100)
print(result)'''
#2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''sayi= int(input('Sayi Gir:'))
result= (sayi>0) and (sayi%2 == 0)
print(f' Sayı pozitif ve çifttir: {result}')'''
#3-E-mail ve Parola bilgileri ile giriş kontrolü yapınız.
'''email= 'hpu@gmail.com'
parola= '123456'
ke=input('Email:')
kp= input('Parola:')
result= (ke== email) and (kp== parola)
print(f' Kullanıcı bilgileri: {result}')'''
#4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''
sayi1= int(input('1.Sayı:'))
sayi2= int(input('2.Sayı:'))
sayi3= int(input('3.Sayı:'))

list= [sayi1, sayi2, sayi3]
list.sort()
print(list)'''
"""sayi1= int(input('1.Sayı:'))
sayi2= int(input('2.Sayı:'))
sayi3= int(input('3.Sayı:'))

result= (sayi1>sayi2) and (sayi1>sayi3)
print(f' En büyük sayı 1.Sayıdır: {result}')

result = (sayi2 > sayi1) and (sayi2 > sayi3)
print(f' En büyük sayı 2.Sayıdır: {result}')

result = (sayi3 > sayi2) and (sayi3 > sayi1)
print(f' En büyük sayı 3.Sayıdır: {result}')"""

#5-Kullanıcıdan iki vize(%60) ve bir final(%40) notu isteyip ortalama hesaplayın
    #Eğer ortalama 50 ve üstündeyse geçti yazdırın, değilse kaldı yazdırın.
    #Ort 50 olsa bile final notu en az 50 olmalıdır
    #finalden 70 alındığında ortalamanın önemi olmasın

'''
vize1= float(input('1.Vize Notu:'))
vize2= float(input('2.Vize Notu:'))
final= float(input('Final Notu:'))

ort= ((vize1+vize2)/2)*0.6 + (final*0.4)

durum1= (ort >= 50)
durum2= (final==50)
durum3= (final==70)

result=(durum3== True) or (durum1== True) and (durum2 == True)

print(f' Dersten geçme durumu: {result}')
'''

#6-Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayın.
    #Formül (kilo/ boy uzunluğunun karesi)
    #Aşağıda ki tabloya göre kişi hangi gruba girmektedir?
    #0-18.4         => Zayıf
    #18.5-24.9      => Normal
    #25-29.9        => Fazla Kilolu
    #30-34,9        => Şişman(Obez)

ad= input('Adınız:')
kilo= float(input('Kilonuz:'))
boy= float(input('Boyunuz:'))

ki= (kilo /(boy)**2)

durum1= (0<ki    and  ki<=18.4)
durum2= (18.5<ki and  ki<=24.9)
durum3= (25<ki   and  ki<=29.9)
durum4= (30<ki   and  ki<=34.9)

print(ki)
print(f' Sn.{ad} kilo indeksinize göre zayıf: {durum1}, normal: {durum2}, fazla kilolu: {durum3}, şişman(obez): {durum4}')