// Автор: Зубов Н.С.
var sum, k, i: longint;
begin
k := 0;
sum:= 0;
  for i := 697 to 3458 do begin
      if (i mod 16=14) and ((i mod 8)=(i mod 7))  then begin
          k := k + 1;
         sum:=sum+i;
      end;
  end;
  writeln(sum,' ' ,k);
end.