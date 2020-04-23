x = 0
n = int(input())
for i in range(n):
  m = input()
  if m == "++X" or m == "X++":
    x += 1
  elif m == "--X" or m == "X--":
    x -= 1
print(x)
