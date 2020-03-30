'''try:
    file=open("newfile.txt", "r")
    print(file)
except FileNotFoundError:
    print("Dosya Bulunamadı...")
finally:
    print("Dosya kapandı.")
    file.close()'''
file= open("newfile.txt","r", encoding="utf-8")
#for döngüsü

'''for i in file:
    print(i, end=" ")
file.close()'''

#***********read() fonksiyonu
"""content1= file.read()
print('İçerik 1')
print(content1)

content2=file.read()
print('İçerik 2')
print(content2)
file.close()"""

#content= file.read(5)
#content= file.read(3)
#content= file.read(2)

#print(content)

#file.close()

#***********readline() fonksiyonu

"""print(file.readline(), end="") #end sayesinde satır arası boşluk olmaz
print(file.readline(), end="")
print(file.readline(), end="")
file.close()"""

#***********readlines() fonksiyonu

liste=file.readlines() #ile dosya içerisindeki her bir satır bir indisle çağırılabilir.
print(liste[0])
print(liste[1])
print(liste[2])

file.close()