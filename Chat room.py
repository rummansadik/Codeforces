n = input()
s = "hello"
f = []
m = []
p = 0
for sn in n:
  if sn in s:
    f.append(sn) 
for j in f:
  if j == s[p]:
    m.append(j)
    p += 1
    if p == 5:
      break
if "".join(m) == s:
  print("YES")
else:
  print("NO")
