import re

line = 'ПрогнозПогоди27.09 Вт28.09 Ср29.09 Чт30.09 Пт1.10 Сб'
shablon = re.compile('\\d{1,2}[.]\\d\\d ..')  # [А-Яа-яЇїІі,]
dates = shablon.findall(line)
print(dates)

line = 'Температура, °C 9..11 14..16 10..12 15..17 10..12 15..17 11..13 18..20 14..16 18..20'
templ = re.compile('\\d{1,2}[.][.]\\d{1,2}')
values = templ.findall(line)
print(values)

tByDay = []
Nv = len(values)
for i in range(0, Nv, 2):
    tByDay.append(values[i]+';'+values[i+1])
    #print(i)
print(tByDay)

Nday = len(dates)
for i in range(Nday):
    print("{:14} - {:>14}".format(dates[i], tByDay[i]))

Nday = len(dates)
sDates = "".join([ "{:14}|".format(dates[i]) for i in range(Nday) ])
sTemps = "".join([ "{:14}|".format(tByDay[i]) for i in range(Nday) ])
print("|",sDates)
print("|",sTemps)

for i in range(Nday):
    print ( "{:14}|".format(dates[i]) )