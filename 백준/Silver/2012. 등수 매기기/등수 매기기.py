import sys
input = sys.stdin.readline

N = int(input())
ranks = [int(input()) for _ in range(N)]


ranks.sort()

ans = 0

for i in range(1, N+1):
    ans += (abs(ranks[i-1] - i))
print(ans)

