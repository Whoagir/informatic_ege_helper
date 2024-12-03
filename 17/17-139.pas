// Автор: В.М. Шелудько
var s, k, max, min, i : integer;
Begin
  s := 0; k := 0;
  max := 2120;
  min := 15470;
  for i:=2381 to 14655 do 
    if (i mod 6 = 0) or (i mod 11 = 0) then
      if (i mod 5 <> 0) and (i mod 7 <> 0) then
        if (i div 100 mod 10 <> i div 10 mod 10 ) then begin
          if i > max then
            max := i;
          s := s + i;
          k := k + 1;
        end;
  writeln( trunc(s/k), ' ', max)
end.








