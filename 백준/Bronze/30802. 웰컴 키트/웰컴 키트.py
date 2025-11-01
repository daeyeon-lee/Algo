N = int(input())
shirts = list(map(int,input().split()))
T, P = map(int,input().split())
ans = []

# 티셔츠 묶음 개수 구하기
for size in shirts:
    # 1이 아닌 5의 배수 이면
    if size % T == 0 and size != 1:
        # 몫
        ans.append(size // T) 
    # 5의 배수가 아니면
    else:
        # 몫 + 1
        ans.append((size // T) + 1) 
print(sum(ans))

# 펜 묶음 개수 구하기
print(N // P, N % P) # 몫 = 묶음 개수 # 나머지 = 낱개 개수
