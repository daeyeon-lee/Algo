N = int(input())

for _ in range(N):
    arr = input()
    cnt = 0
    for i in arr:
        if i == "(":
            cnt += 1
        if i == ")":
            cnt -= 1
            if cnt < 0:
                print("NO")
                break
    else:
        if cnt == 0:
            print("YES")
        else:
            print("NO")

