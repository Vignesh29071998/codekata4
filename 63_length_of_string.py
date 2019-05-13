a = input()
b = []
for i in range(0,len(a)):
  if a[i] not in b:
    b.append(a[i])
  else:
    break
print(len(b))
