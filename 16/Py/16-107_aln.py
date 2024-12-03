#107_Автор задачи А.Л.Наймушин	
def F( n ):
  if n == 0: return 3
  elif 0<n <= 15: return F(n-1)
  elif 15<n < 100: return 2.5*F(n-3)
  
  else:
      if n >= 100:
        return 3.3* F(n-2)
rez = F(100)      
print('F(100) = ',rez )
rez *=10
#print(rez )
otv = int(rez)
print('Ответ = ', otv%10)
#s = str(otv)
#print(s[0])

           

'''
F(100) =  1373900992973.631
Ответ =  6

'''



