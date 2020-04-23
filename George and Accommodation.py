n = int(input())
count = 0
for i in range(n):
	x, y = input().split()
	x, y = int(x), int(y)
	if y - x >= 2:
		count += 1
print(count)
