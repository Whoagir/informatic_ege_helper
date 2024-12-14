# Автор: Д. Муфаззалов

with open('26-j2.txt') as f:
  n = int(f.readline())
  a = sorted(list(map(int, [f.readline() for _ in range(n)] )))

s, m = sorted([sum(a), a[n // 2]*n])
ans = len([1 for i in a if s <= i * n <= m])
print(ans)
