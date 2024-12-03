// Автор: Зубов Н.С.
var i,k,max,d,n,p,m:integer;
begin
  k:=0;
  max:=0;
  for i:=1000 to 70000 do begin
    n:=i;
    d:=0;
    while n>0 do begin
      n:=n div 8;
      d:=d+1;
    end;
    p:=0;
    m:=i;
    while m>0 do begin
      m:=m div 5;
      p:=p+1;
    end;
    if (d=5) and (p=6) and (i mod 16=10) and ((i div 16) mod 16=15) then begin
      k:=k+1;
      max:=i;
    end;
  end;
  writeln(k,' ',max);
end.