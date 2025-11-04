N, K = map(int,input().split())
q = []
for i in range(1,N+1):
    q.append(i)
ans = []
idx = 0
while q:
    idx = (idx + K - 1) % len(q)
    ans.append(q.pop(idx))
print('<'+', '.join(map(str,ans))+'>')
