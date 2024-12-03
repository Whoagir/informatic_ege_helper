# 157) Сколько существует чисел, делящихся на 5, десятичная запись
# которых содержит 6 цифр, причём все цифры различны и никакие две
# чётные и две нечётные цифры не стоят рядом.

def valid(x):
  x = str(x)
  even = "02468"
  odd = "13579"
  for i in range(len(x)-1):
    if x.count(x[i]) > 1:
      return False
    if (x[i] in even and x[i+1] in even) or \
       (x[i] in odd and x[i+1] in odd):
      return False
  return True

count = 0
for x in range(100000, 1000000, 5):
  if valid(x):
    count += 1

print(count)
