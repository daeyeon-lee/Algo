scales = list(map(int,input().split()))
ans = "mixed"
for i in range(7):
    if scales[i] + 1 == scales[i+1]:
        continue
    else:
        break
else:
    ans = "ascending"


for i in range(7):
    if scales[i] - 1 == scales[i+1]:
        continue
    else:
        break
else:
    ans = "descending"

print(ans)