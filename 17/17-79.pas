// Автор: С.П. Пуляшкина
##
uses school;
var z:=(2095..19402).Where(
   x ->(x in Primes(19402)) and 
       (x.digits.First > x.Digits.Last) );
print( z.count );
z.Where(x ->x mod 100=21).Max.Println

