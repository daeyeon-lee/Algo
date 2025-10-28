N = int(input())
cards = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))

cnt_v = {}
for card in cards:
    cnt_v[card] = cnt_v.get(card,0) + 1

ans = []
for num in nums:
    if cnt_v.get(num,0) == 0:
        ans.append(0)
    else:
        ans.append(1)
print(*ans)
