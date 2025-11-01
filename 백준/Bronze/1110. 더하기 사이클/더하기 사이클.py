N = input()
if len(N) == 1:
    N = '0' + N

cnt = 0 # cnt 0부터 시작
num_v = N # N을 num_v로 할당하고 재귀 종료 조건으로 비교

while True: # 계속 반복
    cnt += 1 # cnt 1 올리고
    num_total = str(int(N[0]) + int(N[1])) # 각 자리 수를 더한 값을 num total
    # 원래 숫자인 N의 오른쪽 자리 수와 num_total의 오른쪽 자리수를 이어 붙여 N으로 재할당
    N = N[-1] + num_total[-1]
    
    # N값이 num_v랑 동일하면 반복문 종료 cnt 출력
    if N == num_v:
        break

print(cnt)