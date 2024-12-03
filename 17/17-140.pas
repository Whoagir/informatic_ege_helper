// Автор: В.М. Шелудько
var k, min, i : integer;
Begin
  k := 0;
  min := 13470;
  for i:=4413 to 10153 do 
    if (i mod 5 = 0) and (i mod 23 = 0) then
      if (i mod 10 <> 0) and (i mod 7 <> 0) then
        if (i div 10 mod 10 >=1) and (i div 10 mod 10 <= 3 ) then begin
          if i < min then
            min := i;
          k := k + 1;
        end;
  writeln(k, ' ', min)
end.








