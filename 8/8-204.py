# Автор: А. Куканова

count = 0

even = '02468'
odd = '13579'

for x in range(10 ** 5, 10 ** 6):
    s = str(x)
    if len(set(s)) == 6 and all(not(s[i] in even and s[i+1] in even or s[i] in odd and s[i+ 1] in odd) for i in range(5)):
        count += 1
print(count)