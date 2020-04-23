k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
s=0
for j in range(1, d+1):
    if j%k==0 or j%l==0 or j%m==0 or j%n==0:
        s+=1
print(s)
