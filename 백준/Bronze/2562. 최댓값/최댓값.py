nums = [int(input()) for _ in range(9)]
max_num = 0
idx = 0

for i in range(9):
    if nums[i] > max_num:
        max_num = nums[i]
        idx = i
print(max_num)
print(idx+1)
