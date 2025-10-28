import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

curr = sum(visitors[:X])   
max_sum = curr
cnt = 1                    

for i in range(X, N):
    curr += visitors[i] - visitors[i - X]  
    if curr > max_sum:
        max_sum = curr
        cnt = 1
    elif curr == max_sum:
        cnt += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(cnt)
