# Автор: Д. Муфаззалов
# разбор: https://docs.google.com/presentation/d/1OpgkrEPGC0i1olr7pnPQkF2-MrbQ_lpCWM3MXODdJck/edit#slide=id.p
a, b, k = 0, 1, 16
for i in range(k):
    a, b = b, (a + b) * 3
print(a * 4)
