// Автор: Зубов Н.С.
var sum,i,min:integer;
begin
  sum:=0;
  min:=1179;
  for i:=10 to 1178 do begin
    if (i mod 10<>0) and (i mod 10<>2) and (i mod 10<>6) and (i mod 10<>8) and(i mod 100<>14) then begin
      sum:=sum+i;
      if min>i then min:=i;
    end;
  end;
  writeln(sum,' ',min);
end.