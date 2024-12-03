// Автор: Зубов Н.С.
var s, n: integer;
procedure F( n: integer );
begin
  // writeln(n-5);
  s := s + n-5;
  if n > 1 then begin
    // writeln(n+8);
    s := s + n+8;
    F(n-2);
    F(n-3);
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