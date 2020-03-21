numbers= [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

names=['Hatice', 'Pınar', 'Pelin']
for name in names:
    print(f'My name is {name}')

ad= 'Hatice Pınar' #her bir karakteri yazdırır
for a in ad:
    print(a)

tuple=(1, 2, 3, 4, 5)
for t in tuple:
    print(t)

tuple=[(1,2), (1,3),(3,5),(5,7)]
#1,1,3,5 yazdırır
for (t,y) in tuple:
    print(t)
# 1 2
# 1 3
# 3 5
# 5 7 yazdırır
for (t, y) in tuple:
        print(t,y)

d={'k1':1, 'k2':2, 'k3':3}
#sadece key bilgilerini yazdırır
for i in d:
    print(i)
#değerleri ve key leri yazdırmak için
for i in d.items():
    print(i)