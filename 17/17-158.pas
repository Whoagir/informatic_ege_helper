// Автор В.Н. Шубинкин
##
var a := ReadLines('17-1.txt').Select(t -> t.ToInteger).ToArray;
var maxLen := 0;
var Len := 1;
var count := 0;
for var i := 1 to a.High do
begin
  if a[i] < a[i - 1] then
  begin
    Len += 1;
    if Len > maxLen then
    begin
      maxLen := Len;
      count := 0
    end;
    if Len = maxLen then count += 1
  end
  else Len := 1;
end;
print(maxLen, count)