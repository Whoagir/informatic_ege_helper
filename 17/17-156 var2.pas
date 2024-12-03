// Автор В.Н. Шубинкин
// Эффективный однопроходный алгоритм
##
var n := 10000; // количество элементов подсмотрено в текстовом файле
assign(input, '17-2.txt');
var mx := -20000;
var count := 0;
var pos := 0;
for var i := 1 to n do
begin
  var a := ReadInteger;
  if a > mx then 
    begin
      mx := a;
      pos := i;
      count := 0
    end;
  if a = mx then count += 1;
end;
print(count, pos)