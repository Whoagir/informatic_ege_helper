// Автор В.Н. Шубинкин
##
var a := ReadLines('17-1.txt').Select(t -> t.ToInteger).ToArray;
var count := 0;
var maxEl := -20000;
for var i := 1 to a.High - 1 do
begin
  if (a[i] < a[i - 1]) and (a[i] < a[i + 1]) then
  begin
    count += 1;
    maxEl := max(maxEl, a[i])
  end;
end;
print(count, maxEl)