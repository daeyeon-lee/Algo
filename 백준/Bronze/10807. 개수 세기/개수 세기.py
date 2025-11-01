N = int(input())
nums = list(map(int,input().split()))
V = int(input())

cnt = 0
for i in range(N):
    if nums[i] == V:
        cnt += 1

print(cnt)