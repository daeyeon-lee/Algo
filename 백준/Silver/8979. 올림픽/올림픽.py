N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

ans = None # 내가 구해야 할 K국의 메달 개수
for i in range(N):
    if arr[i][0] == K:
        ans = (arr[i][1],arr[i][2],arr[i][3])
        break

cnt = 0
for j in range(N):
    if (arr[j][1],arr[j][2],arr[j][3]) > ans:
        cnt += 1
print(cnt+1) # 그 수의 +1 값이 등수

