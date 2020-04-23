n = int(input())
a = []
b = []
c = []
for i in range(n):
	x, y, z = input().split()
	x, y, z = int(x), int(y), int(z)
	a.append(x)
	b.append(y)
	c.append(z)
if sum(a) == sum(b) == sum(c) == 0:
	print("YES")
else:
	print("NO")
