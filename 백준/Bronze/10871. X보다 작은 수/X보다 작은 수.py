N, X = map(int,input().split())
arr = list(map(int,input().split()))

ans = []
for i in range(N):
    if arr[i] < X:
        ans.append(arr[i])
print(*ans)