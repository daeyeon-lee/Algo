import heapq
import sys
input = sys.stdin.readline
N = int(input())
hq = []
ans = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if hq:
            ans.append(heapq.heappop(hq))
        else:
            ans.append(0)
    else:
        heapq.heappush(hq,num)
print('\n'.join(map(str,ans)))