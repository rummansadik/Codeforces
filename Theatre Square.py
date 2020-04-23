import math
n, m, a = input().split()
n, m, a = int(n), int(m), int(a)
l = math.ceil(n / a)
b = math.ceil(m / a)
print(l * b)
