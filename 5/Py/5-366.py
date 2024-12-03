def alg( n ):
  bi = f"{255-n:08b}"
  r = ('100' if int(bi,2) % 5 == 0 else '101') + bi[3:]
  return int(r, 2)

print( sum( alg(n) == 180 for n in range(256) ) )

# Автор: Н. Леко

k  = 0 						# счётчик чисел, приводящих к 180
for n in range(256):
    n2 = bin(n)[2:]
    n2 = '0' * (8 - len(n2)) + n2 			# дописываем слева недостающее (до 8 разрядов) кол-во нулей
    n2_invert = ''
    for x in n2:
        n2_invert = n2_invert + str(1 - int(x)) 	# инвертируем разряды числа
    r = int(n2_invert,2)
    if r%5 == 0:
        n2_invert = '100' + n2_invert[3:]
    else:
        n2_invert = '101' + n2_invert[3:]
    r = int(n2_invert,2)
    if r == 180:
        k = k + 1
print(k)
