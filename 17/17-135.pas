// Автор: В.М. Шелудько
var max, min, i : integer;
Begin
  max := 1811;
  min := 9286;
  for i:=1812 to 9285 do 
    if (i mod 8 = 0) or (i mod 19 = 0) then
      if (i mod 4 <> 0) and (i mod 9 <> 0) then
        if (i div 1000 mod 2 <> 0) then begin
          if i > max then
            max := i;
          if i < min then
            min := i;
        end;
  writeln(min, ' ', max)
end.





