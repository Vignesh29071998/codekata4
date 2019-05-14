s = input()
c = 0
if s == s[::-1]:
  print('yes')
else:
  for i in range(len(s)-1,-1,-1):
    if s[i]=='0':
      c = c+1
    else:
      break
  a = '0'*c + s
  if a==a[::-1]:
    print('yes')
  else:
    print('no')
