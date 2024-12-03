// Автор: Зубов Н.С.
var i,k,min,d,n,p,c:integer;
begin
  k:=0;
  min:=8752;
  for i:=331 to 8751 do begin
    d:=0;
    n:=i;
    while n>0 do begin
      n:=n div 10;
      d:=d+1;
    end;
    p:=0;
    c:=i;
    while c>0 do begin
     c:=c div 16;
      p:=p+1;
    end;
    if (d=p) and (i mod 5=0) and (i mod 25<>0) then begin
      inc(k);
      if min>i then min:=i;
    end;
  end;
  writeln(k,' ', min);
end.