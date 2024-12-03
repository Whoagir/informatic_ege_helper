// Автор В.Н. Шубинкин

uses School;

function R(N: integer): integer;
begin
  var N_bi := Bin(N);
  loop 2 do
  begin
    var c1 := N_bi.CountOf('1');
    if c1 mod 2 = 0 then N_bi := N_bi[2:]
    else N_bi := '1'*(c1 + 1)
  end;
  result := Dec(N_bi, 2)
end;


begin
var c := 0;
for var n := 1 to 1000 do c += ord(R(n) = 7);
print(c)
end.