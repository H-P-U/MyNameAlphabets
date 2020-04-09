from datetime import datetime

from datetime import timedelta

simdi=datetime.now() #datetime.today()

result=simdi.year
result=simdi.month
result=simdi.day
result=simdi.hour
result=simdi.minute
result=simdi.second
result=datetime.ctime(simdi)
result= datetime.strftime(simdi, '%Y')
result= datetime.strftime(simdi, '%X')
result= datetime.strftime(simdi, '%d')
result= datetime.strftime(simdi, '%A')
result= datetime.strftime(simdi, '%B')
result= datetime.strftime(simdi, '%Y %A %B')


t='15 April 2020 hour 10:25:20'
td= datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
td=td.year
print(td)

birthday= datetime(1995,2,18,13,30,10)

result= datetime.timestamp(birthday)
result=datetime.fromtimestamp(result)
result=datetime.fromtimestamp(0)
result= simdi-birthday
#result=result.days
print(simdi)
#result=simdi+timedelta(days=10)
result=simdi+timedelta(days=730, minutes=15)
print(result)