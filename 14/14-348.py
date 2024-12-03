# Автор: А. Носкин
# алфавит 18сс
s = "0123456789abcdefgh"
for x in s:
    a1 = "9009"+x
    a2 = "2257"+x
    summ = int(a1,18)+int(a2,18)
    if summ%15==0:
        print(summ//15)
        break


