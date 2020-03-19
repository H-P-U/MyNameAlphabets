'''
Daire alanı: pi r^2
Daire çevresi: 2pir

Yarıçapı verilen dairenin alanını ve çevresini hesaplayınız. pi=3,14

'''
r= float(input ("yari çap: "))
pi= 3.14
daireAlan= pi*(r**2)
daireCevre= 2*pi*r
"""print("alan: ", daireAlan)
print("çevre: ",daireCevre)"""
print('alan: '+ str(daireAlan)+ ' çevre: '+ str(daireCevre))