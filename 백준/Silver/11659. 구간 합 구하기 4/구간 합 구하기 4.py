N, M = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]

ans = []
for _ in range(M):
    i, j = map(int,input().split())
    ans.append(dp[j]-dp[i-1])
print('\n'.join(map(str, ans)))