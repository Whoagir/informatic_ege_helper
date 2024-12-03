# Автор: А. Носкин

count = 0
for a1 in 'ЛУБИНА': # на этом месте нет буквы Г
    for a2 in 'ГУБИНА': # на этом месте нет буквы Л
        for a3 in 'ГЛБИНА': # на этом месте нет буквы У
            for a4 in 'ГЛУИНА': # на этом месте нет буквы Б
                for a5 in 'ГЛУБНА': # на этом месте нет буквы И
                    for a6 in 'ГЛУБИА': # на этом месте нет буквы Н
                        for a7 in 'ГЛУБИН': # на этом месте нет буквы А
                            a = a1+a2+a3+a4+a5+a6+a7
                            if len(set(a)) == 7:
                                print(a)
                                count += 1
print(count)

# Автор: К. Поляков

from itertools import permutations

count = 0
for w in permutations('ГЛУБИНА'):
  if sum( a == b for a, b in zip(w, 'ГЛУБИНА') ) == 0:
    count += 1

print(count)
