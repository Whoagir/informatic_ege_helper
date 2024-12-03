# Автор: А. Носкин
# алфавит 17сс
s = "0123456789abcdefg"
for x in s:
    a1 = "9759"+x
    a2 = "3"+x+"108"
    summ = int(a1,17)+int(a2,17)
    if summ%11==0:
        print(summ//11)
        break


