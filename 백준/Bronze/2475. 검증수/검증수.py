nums = list(map(int,input().split()))
ans = 0
for i in range(len(nums)):
    ans += nums[i] ** 2
ans %= 10
print(ans)
