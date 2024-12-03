// Автор В.Н. Шубинкин
##
var a := ReadLines('17-2.txt').Select(t -> t.ToInteger).ToArray;
var minEl := a.Min;
print(a.CountOf(minEl), a.LastIndexMin + 1)