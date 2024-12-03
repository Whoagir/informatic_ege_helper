// Автор: Зубов Н.С.
var sum, k, i: longint;
begin
k := 0;
sum:= 0;
  for i := 99 to 999 do begin
      if (i mod 16=9) and (i mod 9=8)  then begin
          k := k + 1;
         sum:=sum+i;
      end;
  end;
  writeln(sum,' ' ,k);
end.