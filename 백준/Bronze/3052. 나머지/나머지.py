ans = []
for _ in range(10):
    N = int(input())
    ans.append(N % 42)
ans_v = len(set(ans))
print(ans_v)
