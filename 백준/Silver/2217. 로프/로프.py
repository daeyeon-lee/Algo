N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))
# print(weights)
weights.sort()


ans = 0
for i in range(len(weights)):
    weights_v = weights[i] * (N-i)
    if weights_v >= ans:
        ans = weights_v
print(ans)