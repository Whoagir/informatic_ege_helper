// Автор: В.М. Шелудько
var s, k, max, min, i : integer;
Begin
  s := 0; k := 0;
  max := 2120;
  min := 13470;
  for i:=2121 to 13469 do 
    if (i mod 3 = 0) and (i mod 15 = 0) then
      if (i mod 6 <> 0) and (i mod 12 <> 0) then
        if (i div 100 mod 10 ) mod 3 = 0 then begin
          if i > max then
            max := i;
          if i < min then
            min := i;
        end;
  writeln(max + min)
end.







