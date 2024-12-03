// Автор: В.М. Шелудько
var s, k, max, i : integer;
Begin
  max := 2480;
  for i:=2481 to 14832 do 
    if (i mod 5 = 0) or (i mod 11 = 0) then
      if (i mod 6 <> 0) and (i mod 7 <> 0) then
        if (i mod 10 <> 0) and (i mod 23 <> 0) then begin
          k := k + 1;
          s := s + i;
          if i > max then
            max := i;
        end;
  writeln(s/k, ' ', max)
end.


