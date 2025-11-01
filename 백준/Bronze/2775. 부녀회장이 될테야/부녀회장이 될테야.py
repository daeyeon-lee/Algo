# k층의 n호에 살려면 자신의 아래(k-1)층의 1호부터 n호까지 사람들의 수의 합
# 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

T = int(input())
for _ in range(T):
    k = int(input()) #k층
    n = int(input()) #n호



    zero_floor = []
    for i in range(1,n+1):
        zero_floor.append(i) # 0층 n호 각 인원 리스트로 받기기
  

    num = [0] * (n+1)
    for _ in range(k): # k층 만큼 반복
        for i in range(1,n): # 인덱스 쓸거라 n+1이 아닌 n
            zero_floor[i] += zero_floor[i-1] # 층별 각 호실의 사람 수를 변경

    print(zero_floor[-1]) # n호까지의 인원이니까 마지막 인덱스 출력