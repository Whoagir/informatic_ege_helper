# Автор В.Н. Шубинкин


def f(a):
    for x in range(1, 1000):
        if x & a == 0 and x & 41 != 0 and x & 33 == 0:
            return False
    return True


a = 1
while not f(a):
    a += 1
print(a)
