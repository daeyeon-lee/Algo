N, M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

cnt = 0
for i in B:
    if i not in A:
        cnt += 1

for j in A:
    if j not in B:
        cnt += 1
        
print(cnt)