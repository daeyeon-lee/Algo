N = int(input())

ans = []
for _ in range(N):
    x,y = map(int,input().split())
    ans.append([x,y])


ans.sort(key=lambda x : (x[1],x[0]))
for answer in ans:
    print(*answer)
