// Автор: В.М. Шелудько
var k, s, min, max, i : integer;
Begin
  k := 0; s := 0;
  min := 13470;
  max := 1000;
  for i:=4735 to 8756 do 
    if (i mod 5 = 0) and (i mod 17 = 0) then
      if (i mod 7 <> 0) and (i mod 14 <> 0) then
        if (i div 100 mod 10 <= i div 10 mod 10) then begin
          if i < min then
            min := i;
          if i > max then
            max := i;
          s := s + i;
          k := k + 1;
        end;
  writeln(trunc(s/k) + min + max)
end.










