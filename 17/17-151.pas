// Автор В.Н. Шубинкин
##
var a := ReadLines('17-1.txt').Select(t -> t.ToInteger).ToArray;
var pair_count := 0;
var minEl := 20000;
for var i := 0 to a.High - 1 do
  if (a[i] mod 3 = 0) and (abs(a[i]) mod 10 = 6)
      or (a[i + 1] mod 3 = 0) and (abs(a[i + 1]) mod 10 = 6) then
  begin
    pair_count += 1;
    minEl := min(minEl, a[i], a[i + 1])    
  end;
println(pair_count, minEl)