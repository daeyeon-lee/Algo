N = int(input())
Pi = list(map(int,input().split()))
Pi.sort()

time = 0
ans = 0

for p in Pi:
    time += p
    ans += time

print(ans)
