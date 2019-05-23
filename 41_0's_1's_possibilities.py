a, b = map(int,input().split())
def permutation(p):
  s = ''
  if p <= 1 or a == 1:
    for i in range(0,a+b):
      if i%2 == 0:
        s += '1'
      else:
        s += '0'
    return s
  else:
    k = ((a+b)//3)*3
    for i in range(0,k,3):
      s += '110'
    if abs((a+b)-k) == 1:
      s += '1'
    elif abs((a+b)-k) == 2:
      s += '11'
    return s
if b//a == 2 or b//a == 1:
  print(permutation(b//a))
else:
  print('-1')
