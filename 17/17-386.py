# Автор: Н. Сафронов

def isPrime(n):
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True

s = [int(x) for x in open('17-386.txt')]
a = []

for i in range(len(s) - 2):
    if '3' in str(s[i]) and '3' in str(s[i + 1]) and '3' in str(s[i + 2]):
        if isPrime(s[i] + s[i + 1] + s[i + 2]):
            a.append(s[i] + s[i + 1] + s[i + 2])
print(len(a), min(a))
