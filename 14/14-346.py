# Автор: А. Носкин
# алфавит 15сс
s = "0123456789abcde"
for x in s:
    a1 = "123" + x + "5"
    a2 = "1" + x+ "233"
    summ = int(a1,15)+int(a2,15)
    if summ%14==0:
        print(summ//14)
        break


