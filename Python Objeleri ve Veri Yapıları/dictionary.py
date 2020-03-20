sehirler=['istanbul', 'kocaeli']
plakalar= [34, 41]

'''print(plakalar[sehirler.index('istanbul')])
print(plakalar[sehirler.index('kocaeli')])'''

'''plakalar= { 'kocaeli': 41, 'istanbul': 34}
print(plakalar['kocaeli'])

#ekleme yapılabilir ya da varolan bilgi güncellenebilir
plakalar['ankara']= 6
plakalar['kocaeli']='new value'
print(plakalar)'''

users={
    'hpü':{
        'age': 25,
        'roles': ['admin', 'user'],
        'e-mail': 'hpu@gmail.com',
        'adres': 'İstanbul',
        'telefon': '12356489'

    },
    'epü':{
        'age': 23,
        'roles': ['user'],
        'e-mail': 'epu@gmail.com',
        'adres': 'İstanbul',
        'telefon': '12356489'
    }
}

print(users['hpü']['age'])
print(users['hpü']['roles'][0])