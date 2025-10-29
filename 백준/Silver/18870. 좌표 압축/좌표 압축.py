N = int(input())
nums = list(map(int,input().split()))

# 중복제거 후 오름차순
unique_num = list(set(nums))
unique_num.sort()

# 이 떄 idx값이 결국 좌표압축한 결과
ans = {}
for idx,num in enumerate(unique_num):
    ans[num] = idx


ans_v = []
for num in nums:
    ans_v.append(ans[num])
print(*ans_v)