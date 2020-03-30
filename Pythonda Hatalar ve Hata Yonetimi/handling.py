#Error Handling
"""try:
    x= int(input('x: '))
    y= int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y için 0 girilemez')
except ValueError:
    print('x ve y için sayısal değer girmelisiniz')"""

"""try:
    x= int(input('x: '))
    y= int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError) as h:
    print('yanlış bilgi girdiniz')
    print(h)"""

"""try:
    x= int(input('x: '))
    y= int(input('y: '))
    print(x/y)
except:
    print('yanlış bilgi girdiniz')"""

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x / y)
    except Exception as ex :
        print('yanlış bilgi girdiniz', ex)
    else:
        break
    finally: #tanımlanmış olan değişkenlerin sonlandıırılması, ya da açılan dosyanın kapatılması için kullanılır
        print('try except sonlandı.')