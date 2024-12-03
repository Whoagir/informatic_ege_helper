// Автор: Зубов Н.С.
var del,  s, min,k, i, j: longint;
begin
k := 0;
del := 0;
s:=0;
  for i := 56123 to 97354 do 
    begin
      for j := 1 to i do 
        begin
          if i mod j = 0 then        
          del := del + 1;
      end;
      if del > 35 then 
        begin
          k := k + 1;
          s:=s+i;
      end;
      del := 0;
      end;
  writeln(k,' ' ,s div k);
end.
