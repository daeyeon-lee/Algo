x, y = map(int,input().split())


days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

ans = y
for i in range(1,x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        ans += 31
    if i in [4, 6, 9, 11]:
        ans += 30
    if i == 2:
        ans += 28
result = days[ans % 7]
print(result)


