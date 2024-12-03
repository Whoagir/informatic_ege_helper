// Автор В.Н. Шубинкин
##
var n := 10000; // количество элементов подсмотрено в блокноте
assign(input, '17-1.txt');
var count := 0;
var minS := 20000;
var a := ReadInteger; // первый элемент пары
loop n - 1 do
begin
  var b := ReadInteger; // второй элемент пары
  if (a mod 7 = 0) and (b mod 17 <> 0)
      or (b mod 7 = 0) and (a mod 17 <> 0) then
        begin
          count += 1;
          minS := min(minS, a + b)
        end;
  a := b
end;
print(count, minS)