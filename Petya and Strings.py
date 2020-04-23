x = input()
y = input()
x = x.lower()
y = y.lower()
if x == y:
  print(0)
else:
  for i in range(len(x)):
    if ord(x[i]) > ord(y[i]):
      print(1)
      break
    elif ord(x[i]) < ord(y[i]):
      print(-1)
      break
