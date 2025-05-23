﻿// Автор В.Н. Шубинкин

function is_correct(num: BigInteger): boolean;
begin
  var even_ind_sum := num.ToString[^1::-2].Select(d -> d.ToDigit).Sum;
  var odd_ind_sum := num.ToString[^2::-2].Select(d -> 2 * d.ToDigit div 10 + 2 * d.ToDigit mod 10).Sum;
  result := (even_ind_sum + odd_ind_sum) mod 10 = 0
end;

begin
  var num := 1234567891011121;
  num += 1;
  while not is_correct(num) do num += 1;
  print(num mod 10bi**8)
end.