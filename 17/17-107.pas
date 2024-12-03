// Автор: Зубов Н.С.
var del, k, min, i, j: longint;
begin
k := 0;
del := 0;
min:= 64355;
  for i := 23561 to 64354 do begin
      for j := 1 to i do 
        begin
          if i mod j = 0 then        
          del := del + 1;
      end;
      if del > 20 then begin
          k := k + 1;
          if min > i then min := i;
      end;
      del := 0;
  end;
  writeln(k,' ' ,min);
end.
