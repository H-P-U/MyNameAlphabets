#yöntem 1
'''#import math  #math modülünü çalıştırır

import math as islem #math mdulunun ismini kendi istediğimiz isme dönüştürüp, o isimle çağırabiliyoruz

#value= dir math  #math modülünün içersinde yer alan fonksiyonların isimlerini gösterir
#value= help math #math modülünün içerisinde yer alan fonksiyonların içeriklerini nasıl kullanılacakalrını gösterir
#value = help(math.factorial) #sadece factorial fonksiyonun özelliklerini gösterir
#value= math.sqrt(49)
#value= math.factorial(5)
#value= math.floor(5.9)
#value=math.ceil(5.9)

value=islem.factorial(5)
print(value)'''

#yöntem 2

#from math import * #bu  sayede direk fonksiyon ismini yazarak işlem yaptırabiliyoruz

def sqrt(x):                       #bu fonksiyon aşağıdaki sqr den önce olduğu için bu işleme our eğer ondan sonra yazılırsa diğer işlem gerçekleştirilir.
    print('x:'+ str(x))

from math import factorial, sqrt #sadece bu iki fonk. import edilmiş oldu

#value=factorial(5)
value= sqrt(9)

print(value)