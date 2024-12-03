// Автор: П. Финкель

begin
var kk:integer;
foreach var a in 'ТИМАШЕВСК' do
  foreach var b in 'ТИМАШЕВСК' do
  foreach var c in 'ТИМАШЕВСК' do
  foreach var d in 'ТИМАШЕВСК' do
  foreach var e in 'ТИМАШЕВСК' do
  foreach var f in 'ТИМАШЕВСК' do begin
    var s:=a+b+c+d+e+f;
    var x:=s.countof('А')+s.countof('И')+s.countof('Е');
    var y:=s.countof('Т')+s.countof('М')+s.countof('Ш')+s.countof('В')+s.countof('С')+s.countof('К');
    if (x=y)and('АШ' not in s)and('ША' not in s)and('ИШ' not in s)and('ШИ' not in s)and('ЕШ' not in s)and('ШЕ' not in s)then kk+=1;
    end;
    println(kk);
end.
