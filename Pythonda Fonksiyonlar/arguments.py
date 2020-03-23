"""def changeName(ad):
    a='H'
ad='HPU'
changeName(ad)
print(ad)


def change(n):
    n[0]='İstanbul'
sehirler=['Kocaeli', 'İzmir']
n=sehirler[:] #slicing
n[0]='İstanbul'
print(sehirler)
print(n)"""

'''def add(*params): #tuple olduğu için tek yıldız
    return sum(params)

print(add(10,20))
print(add(10,20,30,40,50))
print(add(10,20,100,70,852,456,45,10,20,358))'''

"""def displayUser(**args): #dictionary olduğu çin iki yıldız

    for key, value in args.items()
        print('{} is {}'.format(key, value))
displayUser(name='Hatice', age= 2, city='istanbul')
displayUser(name='Pınar', age= 20, city='ankara', tel= '123456')
displayUser(name='Unal', age= 2, city='izmir', tel='59879366', email='u@gmail.com')"""

def myFunc(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1='value1', key2='value2')






