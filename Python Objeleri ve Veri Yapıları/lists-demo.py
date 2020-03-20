#1- "BMW, Mercedes, Opel, Mazda" elemanlarını içeren bir liste oluşturun.
#cars= ['BMW', 'Mercedes', 'Opel', 'Mazda']
'''print(cars)'''
#2- liste kaç elemanlıdır?
'''number=len(cars)
print(number)'''
#3-listenin ilk ve son elemanı nedir?
'''ilk= cars[0]
son=cars[3]
print(ilk+' '+son)'''
#4-Mazda değerini Toyota ile değiştirin.
'''cars[-1]= 'Toyota'
print(cars)'''
#5-Mercedes listenin bir elemanı mıdır?
'''result= cars.index('Mercedes')'''
'''result= 'Mercedes' in cars
print(result)'''
#6-Listenin -2 indeksindeki değer nedir?
'''result= cars[-2]
print(result)'''
#7-Listenin ilk 3 elemanını alın.
'''result= cars[0]+' '+ cars[2]+ ' '+ cars[3]
result= cars[0:3]
print(result)'''
#8-Listenin son 2 elemanı yerine Toyota ve Renault değerlerini getirin.
'''cars[-1]= 'Toyota'
cars[-2]= 'Renault'
cars[-2:]= ['Toyota','Renault']
print(cars)'''
#9-Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
'''newcars= cars+ ['Audi'+','+' Nissan']
print(newcars)'''
#10-Listenin son elemanını silin.
'''del cars[-1]
print(cars)'''
#11-Liste elemanlarını tersten yazdırın.
'''newlist= cars[::-1]
print(newlist)'''
#12- Aşağıdaki verileri bir liste içinde saklayın.
        #studentA= Yiğit Bilgi 2010, [70,60,70]
        # studentB= Sena Turan 1999, [80,80,70]
        # studentC= Ahmet Turan 1998, [80,70,90]
studentA=['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB=['Sena','Turan', 1999, [80,80,60]]
studentC=['Ahmet', 'Turan',1998, [80,70,90]]
#13-Liste elemanlarını ekrana yazdırın.
print(studentA)
print(studentB)
print(studentC)
#result= studentA[2]
#result= studentC[2][1]
result= f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)
