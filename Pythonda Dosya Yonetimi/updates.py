#with open("newfile.txt", "r+",encoding="utf-8") as file:  #r+ hem okuma hem yazma modunda açar
    #print(file.read())

#with open("newfile.txt", "r+",encoding="utf-8") as file:
   #file.seek(20)
   # file.write("deneme")

#with open("newfile.txt", "r+",encoding="utf-8") as file:
    #print(file.read())
#**********Sayfa sonunda güncelleme
"""with open("newfile.txt", "a",encoding="utf-8") as file:
    file.write("\nŞevin Dizin")

with open("newfile.txt", "r",encoding="utf-8") as file:
    print(file.read())"""
#**********Sayfa başında güncelleme
#with open("newfile.txt", "r+",encoding="utf-8") as file:
#    content=file.read()
#    content="Fatma Zehra Ünal\n"+content
#   file.seek(0)
#    file.write(content)

#with open("newfile.txt", "r",encoding="utf-8") as file:
#    print(file.read())

#**********Sayfa ortasında güncelleme

#with open("newfile.txt", "r+",encoding="utf-8") as file:
#    list=file.readlines()
#    list.insert(1, "Kardelen Almasulu\n")
#    file.seek(0)
#    for i in list:
#        file.write(i)
#with open("newfile.txt", "r",encoding="utf-8") as file:
#    print(file.read())

with open("newfile.txt", "r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1, "Kardelen Almasulu\n")
    file.seek(0)
    file.writelines(list)
with open("newfile.txt", "r",encoding="utf-8") as file:
    print(file.read())