// Автор: Зубов Н.С.
program abc;
var k,m,d,l,j,max,n:integer;
begin
  k:=0;
  max:=0;
  for n:=3466 to 9081 do begin
    d:=0;
    m:=n;
    while m>0 do begin
    m:= m div 8;
    d:=d+1;
    end;
    j:=0;
    l:=n;
    while l>0 do begin
      l:= l div 10;
      j:=j+1;
      end;
      if (d<>j) and ((n mod 7=1) or (n mod 7=5)) then
      begin
        k:=k+1;
        if n>max then max:=n;
      end;
    end;
  writeln(k,' ',max);
end.