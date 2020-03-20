website= "http://www.sadikturan.com"
course="Python Kursu Baştan Sona Python Programlama Rehberiniz(40 saat)"
#1-" Hello World " karakter dizisinin başındaki ve sonundaki karakterleri silin.
'''sonuc= ' Hello World '.strip()
print(sonuc)'''
#2-"www.sadikturan.com" içindeki sadikturan bilgisi hariç tüm karakterleri silin.
'''sonuc= website.lstrip('http://www.').rstrip('.com')
print(sonuc)'''
'''sonuc='www.sadikturan.com'.strip('w.com')
print(sonuc)'''
#3-'course'karakter dizisinin tüm karakterlerini küçük harf yapın.
'''sonuc= course.lower()
print(sonuc)'''
#4- 'website' karakter dizini içerisinde kaç tane 'a' vardır? (count(a))
'''sonuc= website.count('a')
print(sonuc)
sonuc= wesite.count('www',0,10)'''
#5- website 'www' ile balayıp 'com' ile bitiyor mu?
'''sonuc1=website.startswith('www')
print(sonuc1)
sonuc2=website.endswith('com')
print(sonuc2)'''
#6- 'website' içinde 'com' ifadesi var mı?
#sonuc=website.find('com')
'''sonuc=website.index('com')
print(sonuc)'''
#7-'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
'''sonuc= course.isalpha()
sonuc= 'hello'.isalpha()
sonuc=course.isdigit()
sonuc='12345'.isdigit()
print(sonuc)'''
#8- 'contents' ifadesini satırda 50 karakter iiçerisine yerleştirip sağına ve soluna '*' ekleyin.
'''sonuc='contents'.center(50,'*')
print(sonuc)'''
#9-'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
'''sonuc=course.replace(' ','-')
print(sonuc)'''
#10- 'Hello World' karakter dizisindeki 'World' ifadesini 'There' ile değişitirin.
sonuc= 'Hello World'.replace('World','There')
print(sonuc)
#11- 'course' karakter dizisini boşluk karakterlerinden ayırın.
sonuc= course.split()
print(sonuc)

