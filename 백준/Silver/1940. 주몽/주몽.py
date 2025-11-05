N = int(input())
M = int(input())
nums = list(map(int,input().split()))


nums.sort()

left = 0
right = N-1
cnt = 0
while left < right:
    if nums[left] + nums[right] == M:
        cnt += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] > M:
        right -= 1
    else:
        left += 1
print(cnt)