#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open(dosya_adi, dosya_erisme_modulu)
#dosya_erisme_modulu =>dosyayı hangi amaçla açtığımızı belirtir.

#'w': 'Write' yazma modu. Dosyayı konumda oluşturur. Mevcutta dosya varsa dosya içeriğini silerek ekleme yapar.
'''result=open("newfile.txt", "w")
file.close()'''
"""file=open("C:/users/pnr_a/desktop/newfile.txt", "w")
print(file)
file.close()"""
"""file=open("newfile.txt","w", encoding='utf-8') #Türkçe karakter vb pek çok karakteri sistem 
tanır hale gelir'utf-8'
file.write("HPU")
file.close()"""
#'a': 'Append' ekleme . Dosyayı konumunda yoksa oluşturur.
#file=open("newfile.txt", "a", encoding= 'utf-8')
#file.write("Hatice Pınar Ünal\n")
#file.close()
#'x': 'Create' oluşturma. Dosyayı konumda zaten varsa hata verir.
file=open("newfile2.txt", "x", encoding= 'utf-8')

#'r': 'Write' okuma. Vrsayılan dosya konumda yoksa hata verir.