N = int(input())
cards = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))

ans={}
for num in cards:
    value = ans.setdefault(num, 0);
    ans[num] = value + 1
for j in nums:
    print(ans.get(j,0),end=' ')
