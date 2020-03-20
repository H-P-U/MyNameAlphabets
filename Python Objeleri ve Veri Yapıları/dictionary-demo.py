'''
öğrenciler={
    '120':{
        'ad': 'Ali',
        'soyad' : 'Yılmaz',
        'telefon': '555 555 55 51'
    },
    '125':{
        'ad': 'Can',
        'soyad' : 'Korkmaz',
        'telefon': '555 555 55 52'
    },
    '128':{
        'ad': 'Volkan ',
        'soyad' : 'Yükselen',
        'telefon': '555 555 55 53'
    }
}
'''

#1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içerisinde saklayınız.
#2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.

ogrenciler={}

number= input('öğrenci no:')
name= input('öğrenci adı:')
surname= input('öğrenci soyadı:')
telefon= input('telefon:')

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon': telefon
    }
})

number= input('öğrenci no:')
name= input('öğrenci adı:')
surname= input('öğrenci soyadı:')
telefon= input('telefon:')

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon': telefon
    }
})

number= input('öğrenci no:')
name= input('öğrenci adı:')
surname= input('öğrenci soyadı:')
telefon= input('telefon:')

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon': telefon
    }
})

print(ogrenciler)

ogrNo= input('Öğrenci no:')
ogrenci=ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo}lu öğrencinin adı {ogrenci['ad']} soyadı {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
