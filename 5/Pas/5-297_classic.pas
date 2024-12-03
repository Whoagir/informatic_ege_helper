// Автор В.Н. Шубинкин

function control_sum(num: BigInteger): BigInteger;
begin
  while num > 0 do
  begin
    result += num mod 10;
    num := num div 10;
    var d := num mod 10 * 2;
    result += d div 10 + d mod 10;
    num := num div 10
  end;
end;

begin
  var num := 1000000000000000;
  num += 1;
  while control_sum(num) <> 25 do num += 1;
  print(num mod 10bi**15)
end.