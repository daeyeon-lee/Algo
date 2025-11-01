N = int(input())
commands = []
ans = []
for _ in range(N):
    commands.append(input())

for command in commands:
    if command.split()[0] == "push":
        ans.append(command.split()[1])
    elif command.split()[0] == "pop":
        if ans:
            print(ans[-1])
            ans.pop()
        else:
            print(-1)
    elif command.split()[0] == "size":
        print(len(ans))
    elif command.split()[0] == "empty":
        if ans:
            print(0)
        else:
            print(1)
    elif command.split()[0] == "top":
        if ans:
            print(ans[-1])
        else:
            print(-1)
