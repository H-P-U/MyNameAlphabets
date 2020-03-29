import random

result= random.random() #0.0 ve 1.0 arasında random sayı atar
result= random.random()*100 #0.0-100.0 arasında random sayı atar
result= random.uniform(1,10) #0.0-10.0 arasında random sayı atar
result= int(random.uniform(1,10)) #0.0-10.0 arasında random sayı atar, int sayesindede tam kızımlar yazdırılır
result= random.randint(1,100) #1-100 arasında random tam sayı atar

greeting= 'Hello There'
names=['Ali','Yağmur','Deniz', 'Cenk']
result=names[random.randint(0,len(names)-1)]
result= random.choice(names)
result= random.choice(greeting)

liste=list(range(10))
random.shuffle(liste) #liste elemanlarını karışık sırada verir
result=liste

liste=list(range(100))
result=random.sample(liste,3)
result=random.sample(names,2)


print(result)