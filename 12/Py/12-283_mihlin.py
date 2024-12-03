# Автор: Б.С. Михлин
# 12.283

def fs(s):
  while '555' in s or '888' in s:
    s = s.replace( "555", "8", 1 )
    s = s.replace( "888", "55", 1 )

  return s
n=150
mi8=n+1 # mi8 - min колич.8
for i in range (101,n+1):
  s = i*'8'
  s=fs(s)
  if s.count('8')<mi8:
    mi8=s.count('8')
    mi_8=i # mi_i min длина исходной строки из 8
    mi_s=s # mi_s полученная строка с min колич.8
print (mi_8,mi_s)

#Rez = 101 55




