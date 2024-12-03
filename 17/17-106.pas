// Автор: Зубов Н.С.
var del, k, max, i, j: longint;
begin
k := 0;
del := 0;
max:= 0;
  for i := 12356 to 76435 do begin
      for j := 1 to i do begin
          if i mod j = 0 then 
            del := del + 1;      
      end;
      if del > 15 then begin
          k := k + 1;
          if max < i then max := i;
      end;
      del := 0;
  end;
  writeln(k,' ' ,max);
end.
