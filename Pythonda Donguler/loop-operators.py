"""range

for item in range(50,100,20):  # 50 ve 100 arasındaki sayıları 20 şer arttırarak yazdır
    print(item)
print(list(range(50,100,20)) #50 ve 100 arası 20şer arttırarak liste halinde yazdırır."""

"""enumarate"""

'''index=0
greeting = 'Hello There'

for letter in greeting:
    print({f'index: {index} ,letter:{greeting[index]}'})
    index+=1'''

"""enumerate
greeting = 'Hello There'

for index,letter in  enumerate(greeting):
    print({f'index: {index} ,letter:{letter}'})


greeting = 'Hello'

for item in  enumerate(greeting):
    print(item)"""

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']

print(list(zip(list1,list2)))

for item in zip(list1,list2):
    print(item)

for a,b in zip(list1,list2):
    print(a)