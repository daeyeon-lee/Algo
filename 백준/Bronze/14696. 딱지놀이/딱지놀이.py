def TTakji(A,B):
    A_arr = [0] * 5
    B_arr = [0] * 5
    
    for i in range(1,A[0]+1):
        A_arr[A[i]] += 1
    for j in range(1,B[0]+1):
        B_arr[B[j]] += 1
        
    for k in range(4,0,-1):
        if A_arr[k] == B_arr[k]:
            continue
        else:
            if A_arr[k] > B_arr[k]:
                return "A"
        return "B"
    return "D"



N = int(input()) # N번 라운드
ans = []
for _ in range(N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans.append(TTakji(A,B))
print(*ans, sep = '\n')