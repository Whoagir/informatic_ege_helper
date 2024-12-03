// Автор: С.П. Пуляшкина
##
uses school;
var v:=|5, 11, 17, 19|;
var z:=(10000..20000).Where(
    x -> x.Divisors.Where(y -> y in v).count = 2 );
print( z.count, z.min );


