// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n <= 1 then begin
    Result := 3;
    Exit;
  end;
  if n >1 then
    Result :=F(n-1)+2*F(n-2)-5;
end;
begin
  writeln( F(22) )
end.