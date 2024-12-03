// Автор: Зубов Н.С.
var sum, k, i,j: longint;
begin
k := 0;
sum:= 0;
  for i := 5 to 10000 do begin
    if (i mod 5=0) then begin
      j:=i;
      if (j mod 16=10) and (j mod 7<>0) and (j mod 5=0)  then begin
          k := k + 1;
         sum:=sum+j;
      end;
  end;
  end;
  writeln(sum,' ' ,k);
end.
//536760 108

