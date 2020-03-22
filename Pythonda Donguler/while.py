#1 den 100 e kadar sayıları yaz

"""x=0
while x<100:
    x+=1
    print(x)
print('bitti')

# 1 den 100 e kadar çift sayıları yazdır

x=0
while x<100:
    x+=1
    if x%2==0:
        print(x)
print('bitti')"""

name= '' #False
while not name.strip(): #strip sayesinde boşluk tuşuna basıldığında kodun çalışması yani Merhaba çıktısı  engellenir
    name=input('isminizi giriniz: ')
print(f'Merhaba {name}')