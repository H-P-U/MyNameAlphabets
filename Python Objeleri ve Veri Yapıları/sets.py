fruits={'orange', 'apple', 'banana'}
#print(fruits[0]) indekslenemeezz!!!!

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['grape','mango', 'apple']) #zaten var olan elemanı tekrar yazmaz. update ekler
print(fruits)
fruits.remove('mango') #remove siler
fruits.discard('apple') #siler

fruits.pop()#indekslenemediği için son elemanı sileceği kesin deği herhangi bir silme işlemi yapar

fruits.clear() #tüm elemanları siler

'''myList=[1,2,5,4,4,2,1]

print(set(myList))'''