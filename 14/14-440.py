for x in '0123456789abcdefg':
  a = int(f'12346{x}17', 17) + int(f'7{x}171', 17)
  if a % 16 == 0:
    print(x, a, a // 16)
