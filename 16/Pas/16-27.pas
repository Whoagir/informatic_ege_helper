﻿// Автор: Зубов Н.С.
var s, n: integer;
procedure F( n: integer );
begin
  // writeln(n+1);
  s := s + n+1 ;
  if n > 1 then begin
    // writeln(2*n);
    s := s + 2*n;
    F(n-1);
    F(n-3);
  end;
end; 
begin
  n := 0;
  repeat
    n := n + 1;
    s := 0;
    F(n);
  until s > 1000000;
  writeln( n, ' ', s); 
end.