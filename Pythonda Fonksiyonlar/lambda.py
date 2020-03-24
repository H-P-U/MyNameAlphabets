'''def square(num): return num**2

numbers=[2,3,9,4]

result=list(map(square, numbers)) #eğer list yazmazsan ya da aşağıdaki for döngüsü ile yazmazsan sadece adres belirtir, değer vermez
print(result)

for item in map(square, numbers) #map built in methodu  sayesinde bütün elemanların üzerinde tek tek işlem yapabiliyoruz
    print(item)'''

"""numbers=[2,3,9,4]

result=list(map(lambda num: num**2 , numbers)) #return ve method kullanmadan  formül kullanımı yapılabiliyor LAMBDA ile

print(result)
"""
"""
numbers=[2,3,9,4]
square= lambda num:num**2
result=list(map(square , numbers))
print(result)
"""

'''square= lambda num:num**2
result=square(5)
print(result)'''

numbers=[2,3,9,4,10,12]
"""def check_even(num): return num%2==0
result=(list(filter(check_even,numbers)))
print(result)"""

"""result=(list(filter(lambda num:num%2==0 ,numbers)))
print(result)"""

check_even= lambda num: num%2==0
result=(list(filter(check_even ,numbers)))
print(result)
