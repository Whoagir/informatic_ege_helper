# Автор: А. Носкин

# алфавит 15сс, т.к Х не более 14
s = "0123456789abcde"
for x in s:
    a1 = "131" + x + "1"
    a2 = "13" + x + "3"
    summ = int(a1,15) + int(a2,17)
    if  summ % 11 == 0:
        maxx = summ // 11 # перезаписали
        
print(maxx)
            

