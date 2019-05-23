a, b = map(int,input().split())
def permutation(p,t):
  s = ''
  if p <= 1:
    for i in range(0,a+b):
      if i%2 != 0:
        s += '0'
      else:
        s += '1'
    print(s)
  else:
    k = ((a+b)//3)*3
    for i in range(0,k,3):
      s += t
    if abs((a+b)-k) == 1:
      s += '1'
    elif abs((a+b)-k) == 2:
      s += '11'
    if s[-4:] == '1111':
      permutation(b//a,'110')
    else:
      print(s)
if b//a == 2 or b//a == 1:
  permutation(b//a,'011')
else:
  print('-1')
