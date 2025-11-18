M, N = map(int,input().split())
letters = set()
for _ in range(M):
    letters.add(input())
check_letters = []
for _ in range(N):
    check_letters.append(input())
cnt = 0

for word in check_letters:
    if word in letters:
        cnt += 1
print(cnt)