#1- Kullanıcıdan isim, yaş, eğitim bilgilerini isteyip ehliyet alma durumunu yazdırın.
    # Yaş en az 18 ve eğitim durumu lise veya üniversite olmalıdır.

'''name= input('Adınız:')
age= int(input('Yaşınız:'))
edu= input('Eğitim Durumunuz(İlkokul, Lise ya da Üniversite olarak belirtiniz):')
if (age >= 18):
    if (edu == 'Lise' or edu == 'Üniversite'):
        print('Ehliyet alabilirsiniz.')
    else:
        print('Ehliyet almak için eğitim durumunuz uygun değildir.')
else:
    print('Ehliyet almak için yaşınız uygun değildir')'''

#2-Bir öğrencinin iki not değerini isteyip ortalamasını alarak karşılık geldiği 5 lik notu bilgisini yazdırın
    #0-24  = 0
    #25-44 = 1
    #45-54 = 2
    #55-69 = 3
    #70-84 = 4
    #85-100 = 5
'''not1= float(input('1.Not: '))
not2= float(input('2.Not: '))

ort= (not1+not2)/2

if 0<ort and ort<25:
    print('Not karşılığı 1')
elif 24<ort and ort<45:
    print('Not karşılığı 2')
elif 45<ort and ort<55:
    print('Not karşılığı 3')
elif  55< ort and ort < 70:
    print('Not karşılığı 4')
else:
    print('Not karşılığı 5')'''

#3-Trafiğe çıkış tarihi kullanıcı tarafından girilen bir aracın servis zamanını aşağıdaki bilgilere göre hesaplatın.
    #1.Bakım: 1.yıl
    #2.Bakım: 2.yıl
    #3.Bakım: 3.yıl
    # süre hesabını alınan gün ay yıl bilgisi ışığında gün ay yıl çıktısı verecek şekilde hesaplayın (datetime modül kullanımı gerektirir)

import datetime

tarih= input('Aracınızın trafiğe çıkış tarihini yazınız(yıl/ay/gün):')
tarih= tarih.split('/')
trafigecikis= datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
date= datetime.datetime.now()
fark= date-trafigecikis
days=fark.days

if days<=365:
    print('1.Bakım Zamanı')
elif days<=720:
    print('2.Bakım Zamanı')
elif days<=1085:
    print('3.Bakım Zamanı')
else:
    print('HATALI TARİH')


