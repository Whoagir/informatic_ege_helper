// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n = 1 then begin
    Result := 2;
    Exit;
  end;
  if n >0 then
    Result :=F(n-1)+5*n*n;
end;
begin
  writeln( F(39) )
end.
