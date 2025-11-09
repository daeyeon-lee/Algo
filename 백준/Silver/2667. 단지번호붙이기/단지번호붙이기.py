from collections import deque
# 상하 좌우 방향 설정
dr = [1,-1,0,0]
dc = [0,0,-1,1]

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


ans = []
village_cnt = 0 # 단지의 수
# 시작점 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            q = deque([(i,j)])
            visited[i][j] = True
            village_cnt += 1 # 단지의 수 늘리기

            house_cnt = 1 # 단지 내 가구 수
            while q:
                r,c = q.popleft()
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 1 and visited[nr][nc] == False:
                            q.append((nr,nc))
                            visited[nr][nc] = True
                            house_cnt += 1 # 단지 내 가구 수 늘리기
            ans.append(house_cnt) # 최종 가구 수 ans에 넣기
print(village_cnt) # 총 단지 수
ans.sort()
print('\n'.join(map(str,ans))) # 단지 내 가구 수


