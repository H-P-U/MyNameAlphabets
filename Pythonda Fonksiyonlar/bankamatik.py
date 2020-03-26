#Bankamatk Uygulaması

HaticeHesap={
    'ad':'Hatice Ünal',
    'hesap no': '12345678',
    'bakiye':3000,
    'ekHesap': 2000
}
PinarHesap={
    'ad':'Pinar Ünal',
    'hesap no': '12345678',
    'bakiye':2000,
    'ekHesap': 1000
}

def ParaCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if  hesap['bakiye']>= miktar:
        hesap['bakiye'] -= miktar
        print('Paranızı çekebilirsiniz.')
        BakiyeSorgula(hesap)
    else:
        toplam= hesap['bakiye'] + hesap['ekHesap']
        if toplam>= miktar:
            ekHesapKullanimi= input('Ek hesabınızı kullanmak ister misiniz?: e/h')
            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar = miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-= ekHesapKullanilacakMiktar
                print('Paranızı çekebilirsiniz')
                BakiyeSorgula(hesap)
            else:
                 print('Bakiyeler yetersiz')
        else:
            print('Bakiye Yetersiz')


def BakiyeSorgula(hesap):
    print(f"Hesabınızda {hesap['bakiye']} TL var ve ek hesabınızda {hesap['ekHesap']} tl para var")

ParaCek(HaticeHesap, 4000)
BakiyeSorgula(HaticeHesap)
