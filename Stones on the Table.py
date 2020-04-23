n = int(input())
s = input()
a = s[0]
count = 0
for i in range(1, n):
  if s[i] == a:
    count += 1
  else:
    a = s[i]
print(count)

