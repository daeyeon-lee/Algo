N, M = map(int,input().split())
cards = list(map(int,input().split()))

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum_v = cards[i]+cards[j]+cards[k]
            if ans < sum_v <= M:
                ans = sum_v
                if sum_v == M:
                    break
print(ans)
