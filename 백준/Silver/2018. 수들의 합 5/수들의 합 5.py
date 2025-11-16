N = int(input())

left = 1
right = 1
cnt = 0
sum_v = 0
while True:
    if sum_v < N:
        if right > N:
            break
        sum_v += right
        right += 1

    elif sum_v > N:
        sum_v -= left
        left += 1

    elif sum_v == N:
        cnt += 1
        sum_v -= left
        left += 1


print(cnt)

