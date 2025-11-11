N, Game = input().split()
players = []
max_play = 0
for _ in range(int(N)):
    players.append(input())
players = set(players)
players = list(players)


if Game == 'Y':
    max_play = 1
elif Game == 'F':
    max_play = 2
else:
    max_play = 3

ans = len(players) // max_play
print(ans)

