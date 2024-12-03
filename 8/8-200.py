# Автор: А. Куканова

count = 0
for x in range(100, 1000):
    s = str(x)
    if s[0] <= s[1] <= s[2]:
        count +=1
print(count)