# Автор В.Н. Шубинкин


def f(a):
    for x in range(1, 10000):
        if not ((x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))):
            return False
    return True


a = 1
while not f(a):
    a += 1
print(a)
