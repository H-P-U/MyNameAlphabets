'''x= 10
y=20
z=30'''

x, y, z= 10, 20, 3
#x, y= y, x
"""x += 5              #x= x+5
x -= 5              #x=x-5
x *= 5              #x=x*5
x /= 5              #x=x/5
x %= 5              #x=x%5
x //=5              #x=x//5
y **=5              #y=y**5
y **=z              #y=y**z"""

values= 1, 2, 3, 4, 5
print(values)
print(type(values))
x, y, z* = values #eklenen yıldız ile arta kalan elemanlar yıldız konan elemana dizi şeklinde sıralanır
print(x,y,z)
print(x, y, z[0])