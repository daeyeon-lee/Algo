N = input()

ans = []
for i in range(len(N)):
    ans.append(N[i])

ans.sort(reverse=True)

print(''.join(ans))
