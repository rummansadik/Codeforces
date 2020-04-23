n = input()
count = 0
for i in n:
	if i == "4" or i == "7":
		count += 1
if count == 7 or count == 4:
	print("YES")
else:
	print("NO")
