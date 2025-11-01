N = int(input())

for _ in range(N):
    results = input()
    cnt = 0
    ans = []
    for i in range(len(results)):
        if results[i] == "O":
            cnt += 1
            ans.append(cnt)
        else:
            cnt = 0
            ans.append(cnt)
    print(sum(ans))
