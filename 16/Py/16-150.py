F = [0]*4965
for n in range(4965):
  F[n] = n-1 if n <= 3 else \
         F[n-2] + n//2 - F[n-4] if n % 2 == 0 else \
         F[n-1]*n + F[n-2]

print( F[4952] + 2*F[4958] + F[4964] )

# Автор: А. Бриккер

def g():
    if n < 4:
        return n - 1
    if n % 2:
        return f[n - 1] * n + f[n - 2]
    return f[n - 2] + n // 2 - f[n - 4]

f = [0] * 4965
for n in range(4965):
    f[n] = g()
print(f[4952] + 2 * f[4958] + f[4964])
