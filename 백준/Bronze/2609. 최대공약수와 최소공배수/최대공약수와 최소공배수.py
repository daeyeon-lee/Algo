A, B = map(int,input().split())

idx = []

i = 1
for i in range(1, min(A,B)+1):
    if A % i == 0 and B % i == 0:
        idx.append(i)


ans = max(idx)
result = ans * (A // ans) * (B // ans)


print(ans)
print(result)