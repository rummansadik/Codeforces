t = int(input())
a = [int(i) for i in input().split(" ")]
a.sort()
s = 0
for i in range(0, t, 2):
  s += a[i+1] - a[i]

print(s)
