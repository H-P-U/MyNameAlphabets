"""def usalma(number):
    def inner(power):
        return number**power
    return inner

two=usalma(2)
three=usalma(3)

print(two(3))  #2'3
print(three(4)) #3'4"""

"""def yetki_sorgula(page):
    def inner(role):
        if role=='Admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner
user1= yetki_sorgula("Product Edit")
print(user1("Admin"))"""

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpim(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi=="Toplama":
        return toplam
    else:
        return carpim

toplama=islem("Toplama")
print(toplama(1,2,3,7,85,74))

carpma=islem("Çarpma")
print(carpma(8,9,10))

