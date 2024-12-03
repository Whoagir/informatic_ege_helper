// Автор: Зубов Н.С.
var sum, k, i: longint;
begin
k := 0;
sum:= 0;
  for i := 100 to 1000 do begin
      if (i mod 16=0) and (i mod 3<>0)  then begin
          k := k + 1;
         sum:=sum+i;
      end;
  end;
  writeln(sum,' ' ,k);
end.