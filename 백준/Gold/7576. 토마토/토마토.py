from collections import deque
# 상하좌우

dr = [-1,1,0,0]
dc = [0,0,-1,1]

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
q = deque()
cnt = 0
for i in range(M):
    for j in range(N):
        if arr[j][i] == 1 :
            q.append((j,i))

while q:
    r,c = q.popleft()
    for d in range(4):
        nr,nc = r+dr[d], c+dc[d]
        if 0<=nr<N and 0<=nc<M:
            if arr[nr][nc] == 0:
                q.append((nr,nc))
                arr[nr][nc] = arr[r][c] + 1

max_day = 0
for x in range(M):
    for y in range(N):
        if arr[y][x] == 0:
            print(-1)
            exit()
        else:
            if arr[y][x] > max_day:
                max_day = arr[y][x]

else:
    print(max_day - 1)