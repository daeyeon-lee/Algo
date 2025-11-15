from collections import deque

import sys
input = sys.stdin.readline
ans = []
q = deque()
N = int(input())
for _ in range(N):
    commends = (list(map(int,input().split())))
    if commends[0] == 1:
        q.appendleft(commends[1])
    if commends[0] == 2:
        q.append(commends[1])
    if commends[0] == 3:
        if q:
            ans.append(q.popleft())
        else:
            ans.append(-1)
    if commends[0] == 4:
        if q:
            ans.append(q.pop())
        else:
            ans.append(-1)
    if commends[0] == 5:
        ans.append(len(q))
    if commends[0] == 6:
        if q:
            ans.append(0)
        else:
            ans.append(1)
    if commends[0] == 7:
        if q:
            ans.append(q[0])
        else:
            ans.append(-1)
    if commends[0] == 8:
        if q:
            ans.append(q[-1])
        else:
            ans.append(-1)
print('\n'.join(map(str,ans)))