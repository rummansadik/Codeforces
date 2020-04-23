a = [0]*5
for i in range(5):
  b = [int(j) for j in input().split()]
  a[i] = b
for k in range(5):
  if 1 in a[k]:
    x = a[k].index(1)
    y = k
    break
print(abs(x - 2) + abs(y -2))
