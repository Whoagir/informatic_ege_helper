#108_Автор задачи А.Л.Наймушин	
def F( n ):
  if n == 0: return 1
  elif n >0 and n%2 ==0:
    return F(n-1)+F(n-2)
  elif n >0 and n%2 !=0:
    return 1.5*F(n-1)
    
rez = F(15)      
print('F(15) = ',rez )
f = int(rez)
m = set()

while (f != 0):
    m.add(str(f % 10))
    f = f // 10
  
print('n = ',len(m),';','  m = ', m )
'''
F(15) =  915.52734375
n =  3 ;   m =  {'9', '5', '1'}

'''



