n, k = map(int, input().split())
days, c = 1, 0
a = list(map(int, input().split()))
for i in range(0, n):
  b = 86400-a[i]
  c = c+b
  if c!= k:
    days = days+1
  else:
    break
print(days)

