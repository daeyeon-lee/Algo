N = int(input())
ans = []
for _ in range(N):
    x, y = list(map(int,input().split()))
    ans.append([x,y])
ans.sort(key=lambda x:(x[0],x[1]))

for i in ans:
    print(i[0],i[1])