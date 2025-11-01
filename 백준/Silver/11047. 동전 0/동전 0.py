N, K = map(int,input().split())
cnt = 0
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)


for coin in coins:
    if K == 0:
        break
    if coin > K:
        continue
    cnt += K // coin
    K = K % coin

print(cnt)
