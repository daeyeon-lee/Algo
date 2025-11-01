while True:
    N = input()
    ans = 'yes'
    if N == '0':
        break
    for i in range(len(N) // 2):
        if N[i] != N[-i-1]:
            ans = 'no'
            break
    print(ans)