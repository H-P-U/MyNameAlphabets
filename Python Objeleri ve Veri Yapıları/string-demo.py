website = "www.sadikturan.com"
course= "Phyton Kursu: Baştan Sona Phyton Programlama Rehberiniz(40 saat)"

#1- 'course' karakter diisinde kaç karakter bulunur?
'''length= len(course)
print(length)'''
#2- 'website' içinden wwww karakterlerini alın.
'''result=website[0:3]
print(result)'''
#3- 'website' içinden com karakterlerini alın.
'''result= website[15:18]
print(result)'''
#4- 'course' içinden ilk 15 ve son 15 karakteri alın.
'''result_1= course[0:14]
result_2= course[-15:]
print(result_1)
print(result_2)'''
#5- 'course' içerisindeki karakterleri tersten yazdır.
'''result= course[::-1]
print(result)'''

#name, surname, age, job = 'Hatice Pınar','Ünal', 25, 'Mühendis'
#6- yukarıda verilen ifadelerle aşağıdaki cümleyi yazdırın
# 'Benim adımm Hatice Pınar Ünal, yaşım 25 ve mesleğim Mühendis.'
'''print('Benim adım {} {} , yaşım {} ve mesleğim {}.'.format(name,surname, str(age), job))'''
#7- 'Hello world!' ifadesindeki w karakterini W ile değiştirin.
'''a= 'Hello world!'
a= a[0:6]+'W'+a[-5:]
a.replace('w', 'W')
print(a)'''
#8-'abc'ifadesini yanyana 3 defa yazdırın

x= 'abc'
print(str(x)*3)