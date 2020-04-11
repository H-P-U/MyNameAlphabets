import os
import datetime
result=dir(os)
result=os.name

#dizin değiştirme
#os.chdir('C:\\')
#os.chdir('..\\..')
#klasör oluşturma
#os.mkdir('newdirectory')
#os.makedirs('newdirectory/yeniklasör')
#os.renames("newdirectory", "yeniklasör")
#os.rmdir("newdirctory") #newdirectory isimli klasörü siler
#os.removedirs("yeniklasör/yeniklasör") #yeniklasör altındaki yeniklasör klasörünü siler
#listeleme
#result=os.listdir()
#result=os.listdir('C:\\')
"""for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)"""
#etkin dizin öğrenme
#result= os.getcwd()

#result=os.stat("date.py")
#result=result.st_size/1024
#result=datetime.datetime.fromtimestamp(result.st_ctime)    #oluşturulma tarihi
#result=datetime.datetime.fromtimestamp(result.st_atime)    #son erişilme tarihi
#result=datetime.datetime.fromtimestamp(result.st_mtime)     #değiştirme tarihi

#os.system("notepad.exe")

#path
result=os.path.abspath("_os.py") #dosya yolunu verir
result=os.path.dirname("C:/Users/pnr_a/Desktop/PythonUygulamalar/Advanced Python Modulleri ve Web Scraping/_os.py") #dosya dizinini verir dosya adı olmadan
result=os.path.dirname(os.path.abspath("_os.py"))
result=os.path.exists("_os.py")
result=os.path.exists("C:/Users/pnr_a/Desktop/PythonUygulamalar/Advanced Python Modulleri ve Web Scrapinghh/_os.py")
result=os.path.isdir("C:/Users/pnr_a/Desktop/PythonUygulamalar/Advanced Python Modulleri ve Web Scraping")
result=os.path.isdir("C:/Users/pnr_a/Desktop/PythonUygulamalar/Advanced Python Modulleri ve Web Scraping/_os.py")
result=os.path.isfile("C:/Users/pnr_a/Desktop/PythonUygulamalar/Advanced Python Modulleri ve Web Scraping/_os.py")
result=os.path.join("C:\\", "deneme", "deneme1")
result=os.path.split("C:\\deneme")
result=os.path.splitext("_os.py")
print(result)