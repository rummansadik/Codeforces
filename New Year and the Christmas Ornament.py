y, b, r = input().split()
y, b, r = int(y), int(b), int(r)
n = min(y, b, r)
if n == r:
	print(n * 3 - 3)
elif n == b:
	print(n*3)
else:
	if y + 1 <= b and y + 2 <= r:
		print(n * 3 + 3)
	elif y + 1 <= b and y + 2 > r:
		print(r * 3 - 3)
	
