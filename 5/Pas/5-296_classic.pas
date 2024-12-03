// Автор В.Н. Шубинкин

function is_correct(num: BigInteger): boolean;
begin
  var s: BigInteger;
  while num > 0 do
  begin
    s += num mod 10;
    num := num div 10;
    var d := num mod 10 * 2;
    s += d div 10 + d mod 10;
    num := num div 10
  end;
  result := s mod 10 = 0
end;

begin
  var num := 1234567891011121;
  num += 1;
  while not is_correct(num) do num += 1;
  print(num mod 10bi**8)
end.