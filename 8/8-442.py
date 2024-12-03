# Автор: А. Носкин

s = 'ГЛУБИНА'
count = 0
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        for a7 in s:
                            s1 = a1+a2+a3+a4+a5+a6+a7
                            if len(set(s1)) == 7:
                                    x1 = s1.find("Г")
                                    x2 = s1.find("А")
                                    if  x1 - x2 >1:
                                        count += 1
print(count)


# Автор: К. Поляков

from itertools import permutations

count = 0
for w in permutations('ГЛУБИНА'):
  if w.index('Г') > w.index('А')+1:
    count += 1

print(count)

