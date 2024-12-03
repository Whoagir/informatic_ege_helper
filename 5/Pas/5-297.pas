// Автор В.Н. Шубинкин

function control_sum(num: BigInteger): BigInteger;
begin
  var even_ind_sum := num.ToString[^1::-2].Select(d -> d.ToDigit).Sum;
  var odd_ind_sum := num.ToString[^2::-2].Select(d -> 2 * d.ToDigit div 10 + 2 * d.ToDigit mod 10).Sum;
  result := even_ind_sum + odd_ind_sum
end;

begin
  var num := 1000000000000000;
  num += 1;
  while control_sum(num) <> 25 do num += 1;
  print(num mod 10bi**15)
end.