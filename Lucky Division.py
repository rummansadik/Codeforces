n = input()
f = True
#4,7,47,74,744,474,77,44,444,777,447,477,747,774
for i in n:
  if i != "4" and i != "7":
    f = False
if f == True:
  print("YES")
else:
  n = int(n)
  if n % 4 == 0 or n % 7 == 0 or n % 47 == 0 or n % 74 == 0 or n % 444 == 0 or n % 447 == 0 or n % 474 == 0 or n % 477 == 0 or n % 744 == 0 or n % 747 == 0 or n % 774 == 0 or n % 777 == 0:
    print("YES")
  else:
    print("NO")
