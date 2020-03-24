#aşağıdaki kod çıktısı global x olur , fonksiyon içi dışarıdaki değişkenleri etkilemez, fonksiyonun içindeki işlemleri etkiler.
"""x= 'global x'

def function():
    x= 'local x'
function()
print(x)"""

#Global
name='Hatice'

def ChangeName(new_name):
    #local
    name=new_name
    print(name)

ChangeName('Pınar')
print(name)

##########################################

name= 'global string'

def greeting():
    name= 'Hatice'

    def hello():
        neme= 'Pınar' #burada ki name bilgisini yazdırır, eğer name burda olmazsa ilk name i yazdırır
        print( 'Hello'+ name)

    hello()
greeting()

##################################################

"""x=50
def test(x):
    print('x'+x)

    x= 100
    print(f'changed x to {x}' )

test(x)
print(x) #dışarıda global tanımlanan x değerini verir. Global x i fonksiyon içinde değiştirmek için aşağıdaki kod uygulanır."""

x=50
def test():
    global x # bu sayede fonksiyon içindeki tüm işlemler dışarıdaki x e uygulanır.
    print('x'+x)

    x= 100
    print(f'changed x to {x}' )

test(x)
print(x) #dışarıda global tanımlanan x değerine fonksiyon uygulanır ve değişir.