from collections import deque
import sys
input = sys.stdin.readline

q = deque()
ans = []
N = int(input())

for _ in range(N):
    commands = input().split()

    if commands[0] == "push":
        q.append(commands[1])
    elif commands[0] == "pop":
        if q:
            ans.append(q.popleft())
        else:
            ans.append(-1)
    elif commands[0] == "size":
        ans.append(len(q))
    elif commands[0] == "empty":
        if q:
            ans.append(0)
        else:
            ans.append(1)
    elif commands[0] == "front":
        if q:
            ans.append(q[0])
        else:
            ans.append(-1)
    elif commands[0] == "back":
        if q:
            ans.append(q[-1])
        else:
            ans.append(-1)

print('\n'.join(map(str,ans)))