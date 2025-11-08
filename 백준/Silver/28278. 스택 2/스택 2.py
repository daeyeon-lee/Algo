import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = []
for _  in range(N):
    commands = list(map(int, input().split()))


    if commands[0] == 1:
        stack.append(commands[1])
    elif commands[0] == 2:
        if stack:
            ans.append(stack.pop(-1))
        else:
            ans.append(-1)
    elif commands[0] == 3:
            ans.append(len(stack))
    elif commands[0] == 4:
        if stack:
            ans.append(0)
        else:
            ans.append(1)
    elif commands[0] == 5:
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
print('\n'.join(map(str,ans)))