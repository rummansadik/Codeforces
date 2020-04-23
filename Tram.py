n = int(input())
p = 0
d = []
for i in range(n):
  x, y = input().split()
  x, y = int(x), int(y)
  p -= x
  p += y
  d.append(p)

print(max(d))

