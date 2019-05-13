n,k = map(int,input().split())
c = list(map(int,input().split()))
charge = int(input())
bill = (sum(c)-c[k])//2
if charge == bill:
  print("Bon Appetit")
else:
  print(charge-bill)
