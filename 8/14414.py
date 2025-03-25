from itertools import *
a='012345678'
c=0
comb=product(a,repeat=7)
for i in comb:
    s=''.join(i)
    if s.count('6')==1 and '00' not in s and '11' not in s and '22' not in s and '33' not in s and '44' not in s and '55' not in s and '66' not in s and '77' not in s and '88' not in s and '02' not in s and '20' not in s and '04' not in s and '40' not in s and '06' not in s and '60' not in s and '08' not in s and '80' not in s and '13' not in s and '31' not in s and '15' not in s and '51' not in s and '17' not in s and '71' not in s and '24' not in s and '42' not in s and '26' not in s and '62' not in s and '28' not in s and '82' not in s and '35' not in s and '53' not in s and '37' not in s and '73' not in s and '46' not in s and '64' not in s and '57' not in s and '75' not in s and '68' not in s and '86' not in s:
        c+=1
print(c)