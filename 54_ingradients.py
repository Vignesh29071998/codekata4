n, magic = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print((sum(b)+magic)//sum(a))
