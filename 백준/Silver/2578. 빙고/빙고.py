bingo = [list(map(int,input().split())) for _ in range(5)]
nums_speaking = [list(map(int,input().split())) for _ in range(5)]


speaking = []
for i in range(5):
    for j in range(5):
        speaking.append(nums_speaking[i][j])


for i in range(25):
    for r in range(5):
        for c in range(5):
            # 사회자가 부른 숫자를 빙고에서 0으로 바꾸기
            if bingo[r][c] == speaking[i]:
                bingo[r][c] = 0

    # 빙고 세기
    cnt = 0

    # 가로줄 확인
    for r in range(5):
        sum_v = 0
        for c in range(5):
            sum_v += bingo[r][c]
        if sum_v == 0:
            cnt += 1
            
    # 세로줄 확인
    for c in range(5):
        sum_v = 0
        for r in range(5):
            sum_v += bingo[r][c]
        if sum_v == 0:
            cnt += 1

    # 대각선 1(\)확인
    sum_v = 0
    for r in range(5):
        sum_v += bingo[r][r]
    if sum_v == 0:
        cnt += 1

    # 대각선 2(/) 확인
    sum_v = 0
    for r in range(4,-1,-1):
        sum_v += bingo[r][4-r]
    if sum_v == 0:
        cnt += 1

    if cnt >= 3:
        print(i+1)
        break
