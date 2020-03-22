name= 'Hatice Pınar'

"""for letter in name:
    if letter=='ı':
        break       #döngüden tamamen çıkartır
    print(letter)

for letter in name:
    if letter == 'ı':
        continue  # yazılı olanı çıkartır döngüden ama gerisini devam ettirir
    print(letter)"""

x=0

'''while x<5:
    if x==2:
        break
    print(x)
    x+=1'''

"""while x < 5:
    if x == 2:
        continue
    print(x)
    x += 1"""

"""while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)"""

#1-100  e kadar sayıların toplamını yazdırın.

"""sayac=0
top=0

while sayac<=100:
    sayac+=1
    top+=sayac
    if sayac==101:
        break
    print(top)"""


sayac=0
top=0

while sayac<=100:
    sayac+=1
    if sayac%2==1:
        continue
    top += sayac
print(top)



