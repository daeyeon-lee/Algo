N, M = map(int,input().split())

pokemons = [(input()) for _ in range(N)]
dict_poketmon = {}
for idx, poketmon in enumerate(pokemons):
    dict_poketmon[poketmon] = idx

ans = []


for _ in range(M):
    q = input()
    if q.isdigit():
        ans.append(pokemons[int(q)-1])
    else:
        ans.append(dict_poketmon[q]+1)
for i in range(M):
    print(ans[i])