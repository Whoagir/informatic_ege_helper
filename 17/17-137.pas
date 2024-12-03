// Автор: В.М. Шелудько
var s, k, max, min, i : integer;
Begin
  s := 0; k := 0;
  max := 4854;
  min := 13347;
  for i:=4565 to 13346 do 
    if (i mod 7 = 0) then
      if (i mod 6 <> 0) and (i mod 3 <> 0) then
        if (i div 10 mod 10 + i mod 10) mod 2 = 0 then begin
          k := k + 1;
          if i < min then
            min := i;
        end;
  writeln(k,' ', min)
end.






