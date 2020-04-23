n = input()
m = "NO"
for i in range(len(n) - 6):
  if n[i : 7 + i] == "0000000" or n[i : 7 + i] == "1111111":
    m = "YES"

print(m)
