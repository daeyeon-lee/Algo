N = int(input())

arr = [list(input()) for _ in range(N)]

ans = []
# 심장 찾기
heart = 0
x, y = 0,0 # 심장 위치

for r in range(N):
    for c in range(N):
        if arr[r][c] == '*':
            heart += 1
            if heart == 1:
                x = r + 2
                y = c + 1

# 왼쪽 팔 길이 구하기
left_arm = 0
for r in range(y-1):
    if arr[x-1][r] == '*':
        left_arm += 1


# 오른쪽 팔 길이 구하기
right_arm = 0
for r in range(y,N):
    if arr[x-1][r] == '*':
        right_arm += 1


# 허리 길이 구하기
waist = 0

# 허리 위치
waist_r, waist_c = 0,0
for c in range(x,N):
    if arr[c][y-1] == '*':
        waist += 1
    if arr[c][y-1] == '_':
        waist_r = c
        waist_c = y-1
        break


# 왼쪽 다리 길이
left_leg = 0
for r in range(waist_r, N):
    if arr[r][waist_c-1] == '*':
        left_leg += 1

# 오른쪽 다리 길이
right_leg = 0
for r in range(waist_r,N):
    if arr[r][waist_c+1] == '*':
        right_leg += 1

print(x,y)
print(left_arm, right_arm, waist, left_leg, right_leg)