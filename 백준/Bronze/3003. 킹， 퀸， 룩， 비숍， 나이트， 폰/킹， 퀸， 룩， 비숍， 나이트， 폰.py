chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int,input().split()))
ans = []
for i in range(6):
    if chess[i] != arr[i]:
        ans.append(chess[i]-arr[i])
    else:
        ans.append(0)
print(*ans)





