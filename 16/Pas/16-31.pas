// Автор: Зубов Н.С.
var s, n: integer;
function F( n: integer ): integer;
begin
  if n > 0 then
     Result := (n mod 10)* F(n div 10)
  else
   Result := 1;
  Exit;
end;
begin
  n := 0;
  repeat
    n := n + 1;
    F(n);
  until F(n) > 320;
  writeln( n, ' ', F(n)); 
end.
