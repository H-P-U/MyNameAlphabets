#1-Girilen iki sayıdan hangisi büyüktür?
'''sayi1= input('sayi gir:')
sayi2= input('sayi2:')
B1= (sayi1>sayi2)
B2= (sayi2>sayi1)
print(f'Birinci sayi ikinci sayidan büyüktür {B1}')
print(f'İkinci sayi birinci sayidan büyüktür {B2}')'''
#2-Kullanıcıdan alınan iki vize (%60) ve bir final(%40) notunu alıp ortalama hesaplayınız.
'''Eğer ortalama 50 üzerinde ise geçti değilse kaldı yazdır'''
'''vize1= float(input('1.Vize Notu:'))
vize2= float(input('2.Vize Notu:'))
final= float(input('Final Notu:'))
ort= (((vize1+vize2)/2)*0.6+ (final*0.4))
durum1= (ort < 50)
durum2= (ort >= 50)
print(ort)
print(f'Kaldı {durum1}')
print(f'Geçti {durum2}')'''
#3-Girilen bir sayının tek mi çift mi olduğunu yazdırın.
'''sayi=input('Sayi Girin:')
durum = ((int(sayi)%2) == 0)
print(f'Girdiğiniz sayı çift sayıdır {durum}')'''
#4-Girilen bir sayının pozitif negatif olma durumunu yazdırın.
'''sayi= input('Sayı Girin:')
durum1= (int(sayi)>0)
durum2= (int(sayi)==0)
durum3= (int(sayi)<0)
print(f' Girdiğiniz sayı negatiftir {durum3}')
print(f' Girdiğiniz sayı nötr {durum2}')
print(f' Girdiğiniz sayı pozitiftir {durum1}')'''
#5- Parola ve e-mail bilgilerini isteyip doğruluğunu kontrol edin. (email: hpu@gmail.com, parola: 123456)
'''parola= input('Parola:')
email= input('Email:')
durum1= (int(parola)== 123456)
durum2= (email == 'hpu@gmail.com')
print(f'Parola {durum1}')
print(f'Email {durum2}')'''