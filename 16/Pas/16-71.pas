// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n = 0 then begin
    Result :=5;
  end;
  if n >0 then
    Result :=3*F(n-4);
  if n <0 then
    Result :=F(n+3);
end;
begin
  writeln( F(43) )
end.