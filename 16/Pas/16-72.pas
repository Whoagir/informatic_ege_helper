// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n <= 70 then begin
    Result :=F(n+2)+2*F(n*3);
  end;
  if n >70 then
    Result :=n-50;
end;
begin
  writeln( F(40) )
end.