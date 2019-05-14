a, b = input().split()
c = ''
for i in range(0, len(a)-1):
  c = a[i]
  for j in range(i+1, len(a)):
    c = c+a[j]
    for k in range(0,len(b)-len(c)+1):
      if c == b[k:len(c)+k]:
        flag = 1
        break
      else:
        flag = 0
    if flag==1:
      break
    else:
      continue
  if flag == 1:
    break
  else:
    continue
if flag == 1:
  print('yes')
else:
  print('no')
