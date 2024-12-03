// Автор: Зубов Н.С.
var s, n: integer;
procedure F( n: integer );
begin
  // writeln(n*n);
  s := s + n*n;
  if n > 1 then begin
    // writeln(2*n+1);
    s := s + 2*n+1;
    F(n-2);
    F(n div 3);
  end;
end; 
begin
  n := 0;
  repeat
    n := n + 1;
    s := 0;
    F(n);
  until s > 3200000;
  writeln( n, ' ', s); 
end.