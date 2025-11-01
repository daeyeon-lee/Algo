N = int(input())
A = set(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))
ans = []
for i in arr:
    if i in A:
        ans.append('1')
    else:
        ans.append('0')
print('\n'.join(ans))