from collections import deque

N = int(input())
dq = deque()
ans = []
for _ in range(N):
    commends = input()
    commend = commends.split()[0]
    if commend == "push_front":
        dq.appendleft(commends.split()[1])
    elif commend == "push_back":
        dq.append(commends.split()[1])
    elif commend == "pop_front":
        if dq:
            ans.append(dq.popleft())
        else:
            ans.append(-1)
    elif commend == "pop_back":
        if dq:
            ans.append(dq.pop())
        else:
            ans.append(-1)
    elif commend == "size":
        ans.append(len(dq))
    elif commend == "empty":
        if dq:
            ans.append(0)
        else:
            ans.append(1)
    elif commend == "front":
        if dq:
            ans.append(dq[0])
        else:
            ans.append(-1)
    elif commend == "back":
        if dq:
            ans.append(dq[-1])
        else:
            ans.append(-1)
print('\n'.join(map(str,ans)))