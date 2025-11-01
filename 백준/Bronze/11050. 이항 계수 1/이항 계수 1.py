N, K = map(int,input().split())

upper = [i for i in range(N,0,-1)]
lower = [j for j in range(1,K+1)]

ans_up = 1
ans_down = 1

for i in range(K):
    ans_up *= int(upper[i])
    ans_down *= int(lower[i])

answer = int(ans_up) // int(ans_down)
print(answer)