// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n <=3 then begin
    Result := n;
    Exit;
  end;
  if n<=32 then
    Result := (n div 4) + F(n-3)
  else
    Result := 2 * F(n-5);
end;
begin
  writeln( F(100) )
end.

