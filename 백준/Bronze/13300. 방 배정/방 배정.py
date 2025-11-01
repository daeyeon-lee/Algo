N, K = map(int,input().split())
students = [list(map(int,input().split())) for _ in range(N)]

boys = [0] * 7
girls = [0] * 7

for i in range(N):
    if students[i][0] == 0:
        girls[students[i][1]] += 1
    elif students[i][0] == 1:
        boys[students[i][1]] += 1
ans = 0
for boy in boys[1:]:
    if boy == 0:
        continue
    elif boy % K == 0:
        ans += boy // K
    else:
        ans += (boy // K) + 1
for girl in girls[1:]:
    if girl == 0:
        continue
    elif girl % K == 0:
        ans += girl // K
    else:
        ans += (girl // K) + 1

print(ans)