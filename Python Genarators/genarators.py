"""def cube():
    result=[]


    for i in range(5):
        result.append(j**3)
    return result

print(cube())"""
#generator sayesinde daha az bellek kullanılır
"""def cube():

    for i in range(5):
       yield i**3


iterator=cube()

for i in iterator:
    print(i)"""

generator= (i**3 for i in range(5))  #liste=[i**3 for i im range(5)] /print(liste)

print(generator)
for i in generator:
    print(i)

'''print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))'''



