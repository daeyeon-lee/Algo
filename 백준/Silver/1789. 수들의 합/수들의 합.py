S = int(input())
ans = 0
sum_v = 0
for i in range(1,S+1):
    sum_v += i
    if sum_v == S:
        ans = i
        break
    elif sum_v > S:
        ans = i - 1
        break
print(ans)