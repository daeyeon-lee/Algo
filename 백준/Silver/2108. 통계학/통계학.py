N = int(input())
nums = [int(input()) for _ in range(N)]

## 산술 평균
average = sum(nums) / len(nums)
print(round(average))

## 중앙값
nums.sort()
center = nums[N//2]
print(center)

## 최빈값
dict_v = {}
ans = []
max_num = 0
for num in nums:
    # 개수 세기
    dict_v[num] = dict_v.get(num,0) + 1
# 개수 내림차순으로 정렬
dict_sorted = sorted(dict_v.items(), key= lambda x : x[1], reverse=True)
# 최빈값들 ans에 담기
for key, value in dict_sorted:
    if value >= max_num:
        ans.append(key)
        max_num = value
# 최빈값들이 여러 개인 경우 오름차순 정렬 후 2번째, 1개이면 해당 값 뽑기
ans.sort()
if len(ans) == 1:
    print(*ans)
elif len(ans) >= 2:
    print(ans[1])


## 범위
range_v = max(nums) - min(nums)
print(range_v)

