X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    ans = 1
elif X < 0 and Y > 0:
    ans = 2
elif X < 0 and Y < 0:
    ans = 3
elif X > 0 and Y < 0:
    ans = 4

print(ans)