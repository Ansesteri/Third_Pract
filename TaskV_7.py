n = int(input())
P = [int(x) for x in input().split()]
m = int(input())
Q = [int(x) for x in input().split()]

leng_r = max(n, m) + 1
R = [0] * leng_r
for i in range(leng_r):
    R[i] = (P[i] if i <= n else 0) + (Q[i] if i <= m else 0)
while leng_r > 0 and R[leng_r - 1] == 0:
    leng_r -= 1
if leng_r == 0:
    print(0)
else:
    print(*R[:leng_r])
