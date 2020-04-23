n, k = input().split()
n, k = int(n), int(k)
a = [int(i) for i in input().split()]
count = 0
m = a[k-1]
for j in range(n):
  if a[j] >= m and a[j] > 0:
    count += 1
print(count)
