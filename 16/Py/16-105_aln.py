#105_Aвтор А.Л.Наймушин	
def F( n ):
  if n == 0: return 2
  elif 0<n <= 15: return F(n-1)
  elif 15<n < 95: return 1.6*F(n-3)
  
  else:
      if n >= 95:
        return 3.3* F(n-2)
print(F(33) )
      
otv = int(F(33))
print( otv)

           

'''
otv = 33
Ответ задачи: 3


'''



