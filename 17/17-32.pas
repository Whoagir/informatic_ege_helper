// Автор: Зубов Н.С.
program tridva;
uses crt;
var k,d,m,n,max:integer;
begin
  k:=0;
  max:=0;
  for n:=1000 to 9999 do begin
    m:=n;
    d:=0;
    while m>0 do begin
      m:=m div 6;
      d:=d+1;
    end;
      if (d<=5) and (((n mod 6=3) and (n div 6 mod 6=1)) or ((n mod 6=4) and ( n div 6 mod 6=1))) then begin
        k:=k+1;
        if max<n then max:=n;
      end;
      end;
    writeln(k,' ',max); 
end.