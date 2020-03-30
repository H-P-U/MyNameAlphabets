with open("newfile.txt","r", encoding="utf-8") as file: #with olunca file.close a gerek kalmıyor
    content=file.read(10)
    print(content)
    print(file.tell())
    file.seek(0) #cursor ü istediğin konuma götürür
    content2=file.read(16)
    print(content2)


