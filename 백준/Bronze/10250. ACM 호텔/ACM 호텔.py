T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())


    hotel = [[1] * W for _ in range(H)]
    ans_Y = 0
    ans_X = 0
    sum = 0
    for i in range(W):
        for j in range(H-1,-1,-1):
            sum += hotel[j][i]
            if sum == N:
                ans_Y += H-j
                ans_X += i+1

    if ans_X < 10:
        ans_X = '0'+str(ans_X)
    print(''.join(map(str,(ans_Y,ans_X))))