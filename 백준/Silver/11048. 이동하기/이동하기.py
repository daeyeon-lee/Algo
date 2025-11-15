from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

for r in range(1,N+1):
    for c in range(1,M+1):
        # dp는 1-idx이므로 1개씩 뺴서
        # 위, 아래, 대각선 중 최대값을 찾아서 더해서 dp에 저장
        dp[r][c] = arr[r-1][c-1] + max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

print(dp[N][M])