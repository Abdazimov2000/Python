import datetime as t
x = t.datetime.now()
y = int(input('Enter your year: '))
m = int(input('Enter your month: '))
d = int(input('Enter your day: '))
b = t.datetime(year = y, month = m, day = d)
age = x.year - b.year
mon = x.month - b.month
if x.month == b.month and x.day < b.day:
    age = age - 1
    mon = mon + 12
if x.month == b.month and (x.day > b.day or x.day == b.day):
    pass
if mon < 0:
    mon = mon + 12
    age = age - 1
print(age)
print(mon)
