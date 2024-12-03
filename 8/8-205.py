# Автор: А. Куканова

from itertools import product

even = '024'
odd = '135'

count = 0
for num in product('012345', repeat=5):
    if num[0] != '0' and all(num[i] in even and num[i + 1] in odd or num[i] in odd and num[i + 1] in even for i in range(4)):
        count += 1
print(count)