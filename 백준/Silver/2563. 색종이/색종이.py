N = int(input())

arr = [[0]*100 for _ in range(100)]
for _ in range(N):
    l, d = map(int,input().split())
    
    for r in range(l,l+10):
        for c in range(d,d+10):
            arr[r][c] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            cnt += 1
            
print(cnt)