{83. Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n, при n <= 5,
F(n) = n + F(n / 2 – 3), когда n > 5 и делится на 8,
F(n) = n + F(n + 4) , когда n > 5 и не делится на 8.
Назовите максимальное значение n, для которого возможно 
вычислить F(n).}
##
function f(n:integer): integer;
begin
  if n <= 5 then 
    result := n
  else if n mod 8 = 0 then 
    result := n + f(n div 2-3)
  else 
    result := -999999 // функция неопределена
  end;

for var n:= 1 to 1000 do
begin
  var g := f(n);
  if g > 0 then 
    println (n,g); 
end;
