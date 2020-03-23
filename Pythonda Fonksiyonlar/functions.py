def sayHello(name= 'user'):
   return  'Hello ' + name

msg=sayHello('Pınar')
msg=sayHello('Hatice')
print(msg)

def total(num1, num2):
    return num1+num2

result=total(10,20)
result=total(9,852)

print(result)

def yashesapla(dogumYili):
    return 2020-dogumYili

ageHPU= yashesapla(1995)
ageEPU= yashesapla(1997)
ageSD=yashesapla(1994)

print(ageSD, ageHPU, ageEPU)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
   DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
   INPUT: Dogum yili
   OUTPUT: Hesaplanan yil bilgisi
    '''

    yas= yashesapla(dogumYili)
    a=65- yas

    if a>0:
        print(f'emekliliğinize {a} yıl kaldı')
    else:
        print('zaten emeklisiniz')

EmekliligeKacYilKaldi(1995, 'HPU')
EmekliligeKacYilKaldi(1962, 'OU')

print(help(EmekliligeKacYilKaldi))