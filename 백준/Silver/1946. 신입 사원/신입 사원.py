T = int(input())

for _ in range(T):
    scores = []
    N = int(input())
    for _ in range(N):
        scores.append(list(map(int,input().split())))
    scores.sort()
    best_score = 2e21 # 지금까지 본 사람들 중 최소 등수(면접을 가장 잘 본 사람)
    cnt = 0
    for i in range(N):
        if scores[i][1] < best_score:  # 서류 등수는 낮지만 면접 등수가 높으면 합격
            cnt += 1
            best_score = scores[i][1]
    print(cnt)
