// Автор: В.М. Шелудько
var s, k, max, min, i : integer;
Begin
  s := 0; k := 0;
  min := 13470;
  for i:=4391 to 9875 do 
    if (i mod 17 = 0) or (i mod 11 = 0) then
      if (i mod 2 <> 0) and (i mod 13 <> 0) then
        if (i div 100 mod 10 mod 2 = 0) and (i div 10 mod 10 mod 2 <> 0) then begin
          if i < min then
            min := i;
          s := s + i;
          k := k + 1;
        end;
  writeln( trunc(s/k), ' ', min)
end.









