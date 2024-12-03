// Автор: С.П. Пуляшкина
##
uses school;
var z:=(8800..55535).Where(
    x -> (x.Digits.Product > 35) and (7 in x.Digits));
Println( z.max, z.Count )

