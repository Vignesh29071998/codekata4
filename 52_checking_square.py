a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())
dist = 0
dist1 = ((abs(a1-a2)**2)+(abs(b1-b2)**2))**(1/2)
dist2 = ((abs(a2-a3)**2)+(abs(b2-b3)**2))**(1/2)
dist3 = ((abs(a3-a4)**2)+(abs(b3-b4)**2))**(1/2)
dist4 = ((abs(a1-a4)**2)+(abs(b1-b4)**2))**(1/2)
if dist1 == dist2 == dist3 == dist4:
  print('yes')
else:
  print('no')
