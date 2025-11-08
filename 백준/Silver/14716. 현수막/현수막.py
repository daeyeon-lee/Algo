from collections import deque

# 상하좌우 대각선
dr = [-1,1,0,0,1,-1,1,-1]
dc = [0,0,-1,1,1,-1,-1,1]


M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)] # 방문체크


cnt = 0
# 시작점 찾기
for i in range(M):
    for j in range(N):
        # 1이고 아직 방문하지 않은 곳
        if arr[i][j] == 1 and not visited[i][j]:
            # 새로운 시작점으로 queue 새롭게 생성
            q = deque([(i,j)])
            visited[i][j] = True
            cnt += 1

            while q:
                r,c = q.popleft()
                for d in range(8):
                    nr,nc = r+dr[d], c+dc[d]
                    if 0<=nr<M and 0<=nc<N:
                        if arr[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr,nc))
print(cnt)