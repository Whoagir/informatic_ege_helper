// Автор В.Н. Шубинкин
##
var a := ReadLines('17-1.txt').Select(t -> t.ToInteger).ToArray;
var count := 0;
var minR := 20000;
for var i := 0 to a.High - 1 do
  if a[i] < a[i + 1] then
  begin
    count += 1;
    minR := min(minR, a[i + 1] - a[i])    
  end;
println(count, minR)