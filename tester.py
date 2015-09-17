__author__ = 'brennan'

import datetime


convert = []
ans = []
initial_unit = 'feet'
final_unit = 'inches'
amount = 1
with open('conversions', 'r') as file:
    convert = file.readlines()
for number in convert[convert.index(initial_unit)].split():
    try:
        ans.append(float(number))
    except:
        pass
for number in convert[convert.index(final_unit)].split():
    try:
        ans.append(float(number))
    except:
        pass
print(ans)

