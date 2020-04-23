def dis(n):
	if n[0] == n[1] or n[0] == n[2] or n[0] == n[3] or n[1] == n[2] or n[1] == n[3] or n[2] == n[3]:
		f =  False
	else:
		f = True
	return f

l = int(input())
while True:
	l += 1
	m = dis(str(l))
	if m == True:
		print(l)
		break
