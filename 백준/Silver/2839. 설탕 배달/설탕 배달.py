N = int(input())

cnt_5 = N // 5
ans = -1
while cnt_5 >= 0:
    sugar = N - (cnt_5 * 5)
    if sugar % 3 == 0:
        ans = (cnt_5 + (sugar // 3))
        break
    cnt_5 -= 1
print(ans)
