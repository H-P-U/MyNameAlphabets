'''def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper
@my_decorator #"""sayHello= my_decorator(sayHello)
                #sayHello()""" #@my_decorator ile bu işlem sağlandı
def sayHello(name):
    print("Hello", name)
def sayGreeting():
    print("Greeting")

sayHello("Hatice")'''

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__ +" "+ str(finish - start) + " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    #start=time.time()
    #time.sleep(1)

    print(math.pow(a,b))

    #finish=time.time()
    #print("fonksiyon"+ str(finish-start)+" saniye sürdü.")
@calculate_time
def faktoriyel(num):
    #start = time.time()
    #time.sleep(1)

    print(math.factorial(num))

    #finish = time.time()
    #print("fonksiyon" + str(finish - start) +" "+ " saniye sürdü.")
@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(6)
toplama(10,250)



