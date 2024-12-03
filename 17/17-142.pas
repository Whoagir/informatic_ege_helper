// Автор: В.М. Шелудько
var k, min, max, i : integer;
Begin
  k := 0;
  min := 13470;
  max := 1000;
  for i:=1412 to 7865 do 
    if (i mod 8 = 0) or (i mod 19 = 0) then
      if (i mod 4 <> 0) and (i mod 9 <> 0) then
        if (i div 10 mod 10 + i div 100 mod 10 + i div 1000 + i mod 10 ) mod 5 <> 0 then begin
          if i < min then
            min := i;
          if i > max then
            max := i;
        end;
  writeln(min, ' ', max)
end.









