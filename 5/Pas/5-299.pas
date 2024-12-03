// Автор В.Н. Шубинкин

uses School;

function R(N: integer): integer;
begin
  var N_bi := Bin(N);
  loop 2 do
  begin
    var c1 := N_bi.CountOf('1');
    if c1 mod 2 = 0 then N_bi := N_bi[2:].ToInteger.ToString
    else N_bi := 1 + N_bi + '00'
  end;
  result := Dec(N_bi, 2)
end;


begin
  var n := 1;
  while R(n) <= 100 do n += 1;
  print(n)
end.