a=input()
x,y=0,0
d='E'
for i in a:
  if i=='G':
    if d=='E':
      x+=1
    elif d=='W':
      x-=1
    elif d=='N':
      y+=1
    elif d=='S':
      y-=1
  elif i=='L':
    if d=='E':
      d='N'
    elif d=='N':
      d='W'
    elif d=='W':
      d='S'
    elif d=='S':
      d='E'
  elif i=='R':
    if d=='E':
      d='S'
    elif d=='S':
      d='W'
    elif d=='W':
      d='N'
    elif d=='N':
      d='E'
if x==0 and y==0:
  print('yes')
else:
  print('no')
