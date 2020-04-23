a = [int(i) for i in input().split("+")]
a.sort()
for i in range(len(a)):
  if i != 0:
    print("+", end = "")
  print(a[i], end = "") 

print()
