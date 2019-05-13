a = input()
b = input()
e = ''
for i in range(0,len(a)):
  c = ord(a[i])-96
  d = ord(b[i])-96
  if c+d < 26:
    e = e+chr(ord(chr(c+d+96)))
  else:
    e = e+chr(ord(chr(((c+d)-26)+96)))
print(e)
    
