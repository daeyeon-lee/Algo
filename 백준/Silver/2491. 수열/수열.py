N = int(input())
arr = list(map(int,input().split()))


max_cnt = 0
cnt = 1

dp_1 = [1] * N
dp_2 = [1] * N

for i in range(N-1):
    if arr[i+1] >= arr[i]:
        dp_1[i+1] += dp_1[i]

for i in range(N-1):
    if arr[i+1] <= arr[i]:
        dp_2[i+1] += dp_2[i]
    
ans = max(max(dp_1),max(dp_2))
print(ans)