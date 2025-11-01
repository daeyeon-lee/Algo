N, M  = map(int,input().split())
Nolisten = []
Nosee = []
for _ in range(N):
    Nolisten.append(input())
for _ in range(M):
    Nosee.append(input())

Nolisten.sort()
Nosee.sort()

ans = {}
for i in range(N):
    ans[Nolisten[i]] = ans.get(Nolisten[i],0) + 1
for j in range(M):
    ans[Nosee[j]] = ans.get(Nosee[j],0) + 1


names = []
for k in range(N):
    if ans[Nolisten[k]] > 1:
        names.append(Nolisten[k])
for l in range(M):
    if ans[Nosee[l]] > 1:
        names.append(Nosee[l])
sorted_names = sorted(set(names))
print(len(sorted_names))
for name in sorted_names:
    print(name)