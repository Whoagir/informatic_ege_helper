// Автор: В.М. Шелудько
var
  k, min, i: integer;

begin
  k := 0;
  min := 13487;
  for i := 7525 to 13486 do
    if i mod 7 = 0 then
      if (i mod 6 <> 0) and (i mod 9 <> 0) then
        if (i mod 14 <> 0) and (i mod 21 <> 0) then begin
          k := k + 1;
          if i < min then
            min := i;
        end;
  writeln(k, ' ', min)
end.