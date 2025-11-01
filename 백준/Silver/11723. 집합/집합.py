import sys
input = sys.stdin.readline

S = set()
N = int(input())

for _ in range(N):
    commends = input().split()
    commend = commends[0]

    if commend == "add":
        S.add(int(commends[1]))
    elif commend == "remove":
        if int(commends[1]) in S:
            S.remove(int(commends[1]))
        else:
            continue
    elif commend == "check":
        if int(commends[1]) in S:
            print(1)
        else:
            print(0)
    elif commend == "toggle":
        if int(commends[1]) in S:
            S.remove(int(commends[1]))
        else:
            S.add(int(commends[1]))
    elif commend == "all":
        S = set(range(1,21))
    elif commend == "empty":
        S = set()
