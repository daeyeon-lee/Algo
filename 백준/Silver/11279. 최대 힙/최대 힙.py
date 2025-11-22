import heapq
import sys

input = sys.stdin.readline
hq = []
ans = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(hq,(-num,num))

    else:
        if hq:
            ans.append(heapq.heappop(hq)[1])
        else:
            ans.append(0)
print('\n'.join(map(str,ans)))
