a = int(input())
b = int(input())
c = int(input())
f = []
f.append(a+b+c)
f.append(a+b*c)
f.append(a*b+c)
f.append(a*b*c)
f.append((a+b)*c)
f.append(a*(b+c))

print(max(f))
