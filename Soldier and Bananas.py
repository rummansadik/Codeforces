k, n, w = input().split()
k, n, w = int(k), int(n), int(w)
for i in range(1, w+1):
	n -= k * i
if n < 0:
	print(abs(n))
else:
	print(0)
