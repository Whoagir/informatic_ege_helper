#16.104 Автор А.Л.Наймушин	
def F( n ):
  if n == 0: return 1
  elif 0<n <= 10: return F(n-1)
  elif 10<n <= 100: return 2.2*F(n-3)
  
  else:
      if n >= 100:
        return 1.7* F(n-2) 
otv = int(F(40))
print( otv)
sum = 0
while otv:
    #s += str(x % 6)
    sum = sum + otv % 10
    otv = otv // 10
    
print( "  Сумма цифр числа равна: ", sum)

           

'''
otv = 2655
  Сумма цифр otv равна:  18
  
'''



