import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
paper = [[0] * 1001 for _ in range(1001)]

for i in range(N):
    startr, startc = arr[i][0], arr[i][1]
    width, height = arr[i][2], arr[i][3]

    for r in range(startr, startr+width):
        for c in range(startc, startc+height):
            paper[r][c] = (i+1)


cnt = [0] * (N+1)
for i in range(1,N+1):
    j = i - 1
    startr, startc = arr[j][0], arr[j][1]
    width, height = arr[j][2], arr[j][3]
    for r in range(startr, startr+width):
        for c in range(startc, startc+height):
            if paper[r][c] == i:
                cnt[i] += 1
print(*cnt[1:],sep='\n')