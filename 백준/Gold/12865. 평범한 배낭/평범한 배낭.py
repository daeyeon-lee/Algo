N, K = map(int,input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))


dp = [0] * (K+1)

for w, v in arr:
    for price in range(K, w-1, -1):
        #  이 아이템을 쓰는/안 쓰는 경우 중 최대값
        dp[price] = max(dp[price], dp[price-w]+v)
print(dp[K])
