T = int(input())
nums = [int(input()) for _ in range(T)]

dp0 = [0] * (max(nums) + 1)
dp1 = [0] * (max(nums) + 1)


for num in range(max(nums)+1):
    if num == 0:
        dp0[0] += 1
    elif num == 1:
        dp1[1] += 1
    else:
        dp0[num] = dp0[num - 1] + dp0[num - 2]
        dp1[num] = dp1[num - 1] + dp1[num - 2]

for i in nums:
    print(dp0[i], dp1[i])