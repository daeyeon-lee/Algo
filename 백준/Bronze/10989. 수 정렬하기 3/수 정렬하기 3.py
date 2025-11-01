# 처음에 리스트로 받아서 정렬한 후 출력하니니까 메모리 초과 발생
# -> 카운팅 정렬로 풀어봄
import sys

input = sys.stdin.readline

N = int(input())
temp = [0] * 10001 # 최대 수가 10,000,000

for _ in range(N):
    num = int(input())
    temp[num] += 1

for i in range(1,10001):
    for _ in range(temp[i]): # i를 temp[i]만큼 반복
        print(i)
