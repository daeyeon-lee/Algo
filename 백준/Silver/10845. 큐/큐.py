from collections import deque

ans = deque()
command = []
N = int(input())
for _ in range(N):
    command.append(input())


for i in range(N):
    command_v = command[i].split()
    if command_v[0] == "push":
        ans.append(command_v[1])
    elif command_v[0] == "pop":
        if ans:
            print(ans.popleft())
        else:
            print(-1)
    elif command_v[0] == "size":
        print(len(ans))
    elif command_v[0] == "empty":
        if ans:
            print(0)
        else:
            print(1)
    elif command_v[0] == "front":
        if ans:
            print(ans[0])
        else: 
            print(-1)
    elif command_v[0] == "back":
        if ans:
            print(ans[-1])
        else:
            print(-1)
            