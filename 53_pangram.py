sentence = list(input().lower())
flag = 0
for i in range(97, 123):
  if chr(i) in sentence:
    flag = 1
  else:
    flag = 0
    break
if flag == 1:
  print('yes')
else:
  print('no')
