from collections import deque
# 상하 좌우
dc = [0,0,-1,1]
dr = [-1,1,0,0]

T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # arr 배열 만들기
    for _ in range(K):
        X, Y = map(int,input().split())
        arr[Y][X] = 1

    # 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == False:
                q = deque([(i,j)])
                visited[i][j] = True
                cnt += 1
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r+dr[d], c+dc[d]
                        if 0 <= nr < N and 0 <= nc < M:
                            if arr[nr][nc] == 1 and visited[nr][nc] == False:
                                q.append((nr,nc))
                                visited[nr][nc] = True
    print(cnt)
