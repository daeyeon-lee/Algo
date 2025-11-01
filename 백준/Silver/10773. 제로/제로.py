K = int(input())
ans = []

for _ in range(K):
    num = int(input())

    if num == 0:
        if ans:
            ans.pop(-1)
        else:
            continue
    else:
        ans.append(num)
print(sum(ans))