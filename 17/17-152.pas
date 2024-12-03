// Автор В.Н. Шубинкин
##
var a := ReadLines('17-1.txt').Select(t -> t.ToInteger).ToArray;
var pair_count := 0;
var maxEl := -20000;
for var i := 0 to a.High - 1 do
  if (a[i] mod 9 = 0) and (a[i + 1] mod 9 <> 0) and (abs(a[i + 1]) mod 8 = 3)
      or (a[i + 1] mod 9 = 0) and (a[i] mod 9 <> 0) and (abs(a[i]) mod 8 = 3) then
  {if (a[i] mod 9 = 0) and (abs(a[i + 1]) mod 8 = 3)
      xor (a[i + 1] mod 9 = 0) and (abs(a[i]) mod 8 = 3) then
      - неверное условие, внимательно читайте условие задачи и смотрите пример}
  begin
    pair_count += 1;
    maxEl := max(maxEl, a[i], a[i + 1])    
  end;
println(pair_count, maxEl)