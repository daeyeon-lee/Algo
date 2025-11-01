A, B, V = map(int,input().split())

# 시간초과로 while문 사용 불가
# 올라 갈 수 있는 거리 : B-A
# 남은 거리 : V -B
# (V-B) / (A-B) 로 구했을 때 나누어떨어지지 않으면 + 1 해줘야 한다

if (V-B) % (A-B) == 0: #나누어 떨어지면
    ans = (V-B) / (A-B) # 이게 정답
else: # 나누어 떨어지지 않다면면
    ans = (V-B) / (A-B) + 1 # +1 해야 정답



print(int(ans))