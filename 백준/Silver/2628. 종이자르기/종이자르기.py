W, H = map(int,input().split())
N = int(input())

width = [0,H]
height = [0,W]
for _ in range(N):
    location, num = map(int,input().split())
    
    if location == 0:
        width.append(num)
    if location == 1:
        height.append(num)
width.sort()
height.sort()

ans_width = []
for i in range(len(width)-1):
    ans_width.append(abs(width[i]-width[i+1]))

ans_height = []
for i in range(len(height)-1):
    ans_height.append(abs(height[i]-height[i+1]))


ans = max(ans_width) * max(ans_height)
print(ans)