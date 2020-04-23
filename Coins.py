n, s = input().split(" ")
n = int(n)
s = int(s)

if s <= n:
  print("%d" %1)
elif s % n == 0:
  print("%d" %(s/n))
else:
  print("%d" %((s/n) + 1))
