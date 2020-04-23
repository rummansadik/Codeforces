n = int(input())
s = input()
i = 0
j = 1
a = []
while True:
	f = s[i : i+1]
	i = i +j
	j += 1
	a.append(f)
	if i >= len(s):
		break
print("".join(a))
