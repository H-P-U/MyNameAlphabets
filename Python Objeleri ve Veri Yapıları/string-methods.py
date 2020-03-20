message= 'Hello there.I am Hatice Pınar Ünal'
#message= message.upper()
#message= message.lower()
#message= message.capitalize()
#message= message.title()

'''Strip methodu Yazının başındaki ve sonundaki boşlukları ortadan kaldırır'''
#message= message.strip()
'''Split methodu metindeki boşluklara göre kelimeleri ayırır ve gruplandırır, parantez içine şart koyarsak(örn('.') vb) o şata göre ayırma yapar'''
#message= message.split('.')
#message= message.split()
#print(message[1])
'''join methodu ayrılan karakterleri birleştirir ve başına tırnk içerisinde eklediğiniz karakteri aralara yerleştirir'''
#message= ' '.join(message)
#print(message)
'''find methodu içerisine yazılan kelimeyi cümlede aratır ve kelimenin cümle içerisinde başladığı indeks sayısını yazdırı, eğer yoksa negatif değer yazdırır'''
#index= message.find('Hatice')
#print(index)
'''starswith() methodu cümlenin parantez içerisinde belirtilen ifade ile başlayıp başlamadığını, endswith() ise bitip bitmediğini bulur'''
#isFound= message.startswith('P')
#isFound= message.endswith('l')
#print(isFound)

'''replace('','') methodu ilk yazılı olan dizini bulur ve ikinci yazılan dizin ile değiştirir'''
#message= message.replace('Hatice', 'Elif')\
#                .replace('Pınar', 'Pelin')
#print(message)

'''center() methodu ile cümle belirlenen uzunlukta bir konteynerın içerisinde merkezlenir'''
#message= message.center(100)
message= message.center(50, '%')
print(message)