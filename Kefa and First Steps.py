n = int(input())
a = [int(i) for i in input().split()]
m = 0
b = []
c = []

for i in range(n-1):
	if a[i] <= a[i+1]:
		if len(b) == 0:
			b.append(a[i])
		b.append(a[i+1])
	else:
		c.append(b)
		b = []
c.append(b)
f = 0
for k in range(len(c)):
	if f < len(c[k]):
		f = len(c[k])
if f == 0:
	f += 1	
print(f)
