// Автор: В.М. Шелудько
var s, k, max, min, i : integer;
Begin
  s := 0; k := 0;
  max := 4854;
  min := 7857;
  for i:=4855 to 7856 do 
    if (i mod 6 = 0) and (i mod 15 = 0) then
      if (i mod 7 <> 0) and (i mod 16 <> 0) then
        if (i div 100 mod 10 + i div 10 mod 10) mod 2 = 0 then begin
          s := s + i;
          k := k + 1;
          if i > max then
            max := i;
          if i < min then
            min := i;
        end;
  writeln(round(s/k) + min + max)
end.





