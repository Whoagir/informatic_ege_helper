# Автор: Б.С. Михлин
# 12.282

def fs(s):
  while '555' in s or '888' in s:
    s = s.replace( "555", "8", 1 )
    s = s.replace( "888", "55", 1 )

  return s
n = 150
mi5 = n + 1 # mi5 - min колич.8
for i in range (101,n+1):
  s = i*'8'
  s = fs(s)
  if s.count('5')<mi5:
    mi5 = s.count('5')
    mi_5 = i # mi_i min длина исходной строки из 8
    mi_s = s # mi_s полученная строка с min колич.8
print (mi_5,mi_s)

#Rez = 107 88





