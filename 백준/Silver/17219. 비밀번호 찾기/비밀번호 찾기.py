N, M = map(int,input().split())
memo = {}
for _ in range(N):
    url, password = input().split()
    memo[url] = password

for _ in range(M):
    find_url = input()
    print(memo[find_url])
