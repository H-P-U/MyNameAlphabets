#1-Girilen bir sayının 0 ve 100 arasında olup olmadığını kontrol edin.
'''sayi= int(input('Sayı Gir:'))

if 0<sayi and sayi<100:
    print('Girdiğiniz sayı 0 ve 100 arasındadır')
else:
    print('Girdiğiniz sayı 0 ve 100 arasında değildir.')'''
#2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin.
'''sayi= int(input('Sayi Gir:'))

if sayi>0 and sayi%2==0:
    print('Girdiğiniz sayı pozitif çift sayıdır')
elif sayi>0 and sayi%2!=0:
    print('Girdiğiniz sayı pozitiftir ancak çift değildir.')
else:
    print('Girdiğiniz sayı pozitifte çiftte değildir.')'''
#3- email ve parola bilgileri ile giriş kontrolü yapın
'''email='hpu@gmail.com'
parola= 12345

ke= input('Email:')
kp= int(input('Parola:'))

if ke==email and kp==parola:
    print('Hoşgeldiniz:)')
elif ke==email and kp!=parola:
    print('Parola biilgisi yanlış')
elif ke!=email and kp== parola:
    print('Email bilgisi yanlış')
else:
    print('Email ve Parola bilgileri yanlış')'''
#4-Girilen 3 sayıyı büyüklük olarak karşılaştırın

'''a=int(input('Sayi1: '))
b=int(input('Sayi2: '))
c=int(input('Sayi3: '))

if a<b and a<c:
    print('1.Sayı en küçük')
elif b<a and b<c:
    print('2.Sayı en küçük')
else:
    print('3.Sayı en küçük')'''
#5-Kullanıcıdan iki vize(%60) ve bir final(%40) notu isteyip ortalama hesaplayın
    #Eğer ortalama 50 ve üstündeyse geçti yazdırın, değilse kaldı yazdırın.
    #Ort 50 olsa bile final notu en az 50 olmalıdır.
    #finalden 70 alındığında ortalamanın önemi olmasın.

'''vize1= float(input('1.Vize Notu:'))
vize2= float(input('2.Vize Notu:'))
final= float(input('Final Notu:'))

ort= ((vize1+vize2)/2)*0.6 + (final*0.4)


if (final==70) or (ort>= 50) and (final == 50):
    print('TEBRİKLER:) GEÇTİNİZ')
else:
    print('KALDINIZ:(')'''

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

if (0<ki)    and  (ki<=18.4):
    print(f'{ad} kilo indeksin {ki} ve  Zayıfsın beybi az yemek ye')
elif (18.5<ki) and  (ki<=24.9):
    print(f'{ad} kilo indeksin {ki} ve Normalsin bebi :)')
elif (25<ki)   and  (ki<=29.9):
    print(f'{ad} kilo indeksin {ki} ve Bayağı bayağı kilolusun bebi')
elif (30<ki)   and  (ki<=34.9):
    print(f'{ad} kilo indeksin {ki} ve Geçmiş olsun annneeeeemmm obezsin')
else:
    print('En yakın bariatri servisine mi gitsen yavrum')


