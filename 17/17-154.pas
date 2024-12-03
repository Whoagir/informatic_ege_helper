// Автор В.Н. Шубинкин
##
var a := ReadLines('17-1.txt').Select(t -> t.ToInteger).ToArray;
var count := 0;
var minDist := 10000;
var pos := -1;
for var i := 1 to a.High - 1 do
begin
  if (a[i] > a[i - 1]) and (a[i] > a[i + 1]) then
  begin
    count += 1;
    if pos <> -1 then minDist := min(minDist, i - pos);
    pos := i
  end;
end;
print(count, minDist)