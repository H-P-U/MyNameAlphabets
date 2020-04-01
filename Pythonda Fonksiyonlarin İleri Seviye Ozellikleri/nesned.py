"""def greeting(name):
    print('hello',name)

#print(greeting('Ali'))
#print(greeting())

sayHello = greeting

print(sayHello)
print(greeting)

del sayHello
print(greeting) #adresi yazdırır çünkü del ile adres değil sadece name silindi
print(sayHello) #name error verir"""

#encapsulation
'''def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1+1
    num2=inner_increment(num1)
    print(num1, num2)
outer(10)
#inner_increment(10) #çalışmaz outer altında çalıştığı için'''

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise TypeError("number must be zero or pozifive value")

    def inner_factorial(number):
        if number<=1:
            return 1
        return number*inner_factorial(number-1)

try:
    print(factorial(4))
except Exception as ex:
    print(ex)


