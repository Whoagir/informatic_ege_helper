// Автор: Зубов Н.С.
program abc;
var d,n,max,k:integer;
begin
  k:=0;
  max:=0;
  for n:=4563 to 7912 do begin
    if (n mod 7=0) and ((n mod 10) + (n div 1000)>10) then begin
      k:=k+1;
      if max<n then max:=n;
    end;
  end;
  writeln(max,' ',k);
end.