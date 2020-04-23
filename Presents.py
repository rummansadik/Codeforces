t = int(input())
a = [int(j) for j in input().split()]
b = [0] * t
for k in range(t):
    b[a[k] - 1] = k + 1
for l in range(t):
    if l == t-1:
        print(b[l])
    else:
        print(b[l], end = " ")
