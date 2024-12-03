// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n <= 1 then begin
    Result := 2;
    Exit;
  end;
  if n >1 then
    Result :=F(n-1)+F(n-2)+2*n+4;
end;
begin
  writeln( F(25) )
end.
