// Автор: Зубов Н.С.
var sum, k, i: longint;
begin
k := 0;
sum:= 0;
  for i := 12094 to 20075 do begin
      if (i mod 16=15) and (i mod 8<>0) and (i mod 3=0) and (i mod 14<>0) and (i mod 19<>0)  then begin
          k := k + 1;
         sum:=sum+i;
      end;
  end;
  writeln(sum,' ' ,k);
end.