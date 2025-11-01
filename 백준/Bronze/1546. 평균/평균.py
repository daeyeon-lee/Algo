N = int(input())
sco = list(map(int,input().split()))
M = max(sco)

for i in range(N):
    sco[i] = sco[i] / M * 100
ans = sum(sco) / N
print(ans)