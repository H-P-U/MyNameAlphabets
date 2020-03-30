#liste=["1","2","5a","10b","abc"]

#1: liste elemanları içerisindeki sayısal elemanları bulunuz.
"""for x in liste:
    try:
        result= int(x)
        print(result)
    except ValueError:
        continue"""
#2: Kullanıcı q değeri girmedikçe aldığınız her inputun sayısal değerinin olduğundan emin olunuz
# aksi taktirde hata mesajı gönderiniz

"""while True:
    sayi= input('Sayı Gir:')
    if sayi=='q':
        break
    try:
        result= float(sayi)
        print('Girdiğiniz Sayi:', result)
    except ValueError:
        print('Geçersiz Sayı')
        continue"""


#3: Girilen parola içerisinde türkçe karakter hatası verin.

"""def check_password(psw):
    import re
    if re.search("[ü,ç,ş,ğ,ö,İ,ı]", psw):
        raise Exception('Parolada Türkçe karakter bulunamaz.')
    else:
         print('Parola Uygun')


psw = input('Parola:')

try:
    check_password(psw)
except Exception as ex:
    print(ex)"""

#4:Faktöriyel fonksiyonu oluşturup, fonksiyona gelen değerler için hata mesajı gönderin.

def faktoriyel(x):
    x=int(x)

    if x<0:
        raise ValueError('Negatif Değer')
    result=1

    for i in range(1,x+1):
        result*=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
