#this code perfectly gives expected output in python idle
a=int(input())
d,m=[],[]
for i in range(0,2**a):
  b='{:2b}'.format(i)
  if len(b)<a:
    c='0'*(a-len(b))+b
    d.append(c)
  else:
    d.append(b[-a:])
for i in range(0,len(d)):
  p=list(d[i])
  if ' ' in p:
    k=p.index(' ')
    p[k]='0'
  m.append(''.join(p))
for i in m:
  print(i)
