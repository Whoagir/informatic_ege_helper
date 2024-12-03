// Автор: Зубов Н.С.
var i,k,max,d,n:integer;
begin
  k:=0;
  max:=0;
  for i:=1 to 99999999 do begin
    n:=i;
    d:=0;
    while n>0 do begin
      n:=n div 7;
      d:=d+1;
    end;
    if (d=7) and (i mod 3=2) and (i mod 8<>3) and (i mod 12<>5) then begin
      k:=k+1;
      max:=i;
    end;
  end;
  writeln(k,' ',max);
end.